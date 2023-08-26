from typing import Optional, Iterator, Callable, Set

import llm
import torch
import transformers
from transformers import AutoTokenizer


@llm.hookimpl
def register_models(register: Callable[[llm.Model, Optional[Set[str]]], None]):
    register(CodeLlama("CodeLlama-7b-hf"), aliases=("codellama-7b",))
    register(CodeLlama("CodeLlama-13b-hf"), aliases=("codellama-13b",))
    register(CodeLlama("CodeLlama-34b-hf"), aliases=("codellama-34b",))

    register(CodeLlama("CodeLlama-7b-Python-hf"), aliases=("codellama-7b-python",))
    register(CodeLlama("CodeLlama-13b-Python-hf"), aliases=("codellama-13b-python",))
    register(CodeLlama("CodeLlama-34b-Python-hf"), aliases=("codellama-34b-python",))

    register(CodeLlama("CodeLlama-7b-Instruct-hf"), aliases=("codellama-7b-instruct",))
    register(
        CodeLlama("CodeLlama-13b-Instruct-hf"), aliases=("codellama-13b-instruct",)
    )
    register(
        CodeLlama("CodeLlama-34b-Instruct-hf"), aliases=("codellama-34b-instruct",)
    )


class CodeLlama(llm.Model):
    def __init__(self, model_id: str):
        self.model_id = model_id

    def __str__(self) -> str:
        return f"CodeLlama: {self.model_id}"

    def execute(
        self,
        prompt: llm.Prompt,
        stream: bool,
        response: llm.Response,
        conversation: Optional[llm.Conversation],
    ) -> Iterator[str]:
        model = f"codellama/{self.model_id}"
        tokenizer = AutoTokenizer.from_pretrained(model)
        pipeline = transformers.pipeline(
            "text-generation",
            model=model,
            torch_dtype=torch.float16,
            device_map="auto",
        )
        with torch.no_grad():
            sequences = pipeline(
                prompt.prompt,
                do_sample=True,
                top_k=10,
                temperature=0.1,
                top_p=0.95,
                num_return_sequences=1,
                eos_token_id=tokenizer.eos_token_id,
                max_length=200,
            )
            for seq in sequences:
                yield seq["generated_text"]

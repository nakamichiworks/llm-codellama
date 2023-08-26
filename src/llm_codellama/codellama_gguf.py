from typing import Optional, Iterator, Callable, Set

import click
import llm
from huggingface_hub import hf_hub_download
from llama_cpp import Llama

types = ["", "-Python", "-Instruct"]
sizes = ["-7B", "-13B", "-34B"]
quantization_types = [
    "Q2_K",
    "Q3_K_L",
    "Q3_K_M",
    "Q3_K_S",
    "Q4_K_M",
    "Q4_K_S",
    "Q5_K_M",
    "Q5_K_S",
    "Q6_K",
    "Q8_0",
]
MODELS = {
    f"codellama{s.lower()}{t.lower()}.{q}": {
        "repo_id": f"TheBloke/CodeLlama{s}{t}-GGUF",
        "filename": f"codellama{s.lower()}{t.lower()}.{q}.gguf",
    }
    for t in types
    for s in sizes
    for q in quantization_types
}


@llm.hookimpl
def register_models(register: Callable[[llm.Model, Optional[Set[str]]], None]):
    for model_id in MODELS.keys():
        register(
            CodeLlamaGGUF(model_id),
            aliases=(model_id.lower().replace("_", "-").replace(".", "-"),),
        )


@llm.hookimpl
def register_commands(cli: click.Group):
    @cli.group()
    def codellama():
        "Commands for working with CodeLlama"

    @codellama.command()
    @click.argument("model_id", type=click.Choice(MODELS.keys()))
    def download(model_id: str):
        "Download the model file"
        hf_hub_download(
            repo_id=MODELS[model_id]["repo_id"],
            filename=MODELS[model_id]["filename"],
        )


class CodeLlamaGGUF(llm.Model):
    def __init__(self, model_id: str):
        self.model_id = model_id

    def __str__(self) -> str:
        return f"CodeLlama (GGUF): {self.model_id}"

    def execute(
        self,
        prompt: llm.Prompt,
        stream: bool,
        response: llm.Response,
        conversation: Optional[llm.Conversation],
    ) -> Iterator[str]:
        model_path = hf_hub_download(
            repo_id=MODELS[self.model_id]["repo_id"],
            filename=MODELS[self.model_id]["filename"],
        )
        model = Llama(model_path=model_path, verbose=False)
        output = model(prompt.prompt)
        return [output["choices"][0]["text"]]

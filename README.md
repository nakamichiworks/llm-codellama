# llm-codellama

[llm](https://llm.datasette.io/) plugin for [CodeLlama](https://github.com/facebookresearch/codellama) models.

## installation

Install [llm](https://llm.datasette.io/) CLI first.

Then install the plugin by running the following command:

```sh
llm install git+https://github.com/nakamichiworks/llm-codellama.git@main
```

## Usage 

You can use the [original CodeLlama models](https://huggingface.co/codellama) and their [GGUF versions](https://huggingface.co/TheBloke/CodeLlama-7B-GGUF).

Following example generates code using [CodeLlama-7B-Python-GGUF](https://huggingface.co/TheBloke/CodeLlama-7B-Instruct-GGUF):

```sh
llm -m codellama-7b-instruct-q4-k-m "[INST]Write a hello-world program with Python.[/INST]"
```

>   Sure! Here is an example of a "Hello, World!" program in Python:
> ```
> print("Hello, World!")
> ```
> This program will output the string "Hello, World!" to the console. When you run this program, it will print the string to the console and then exit.
> 
> To run this program, you can simply type `python` in your or command prompt, by the name of the file that this program (e.g. `hello_world.py`). For example:
> ```
> $ python hello_world.py
> Hello, World!
> ```

## Supported models

All supported CodeLlama models can be listed with `llm models` command.

```sh
llm models | grep codellama
```

```
CodeLlama (GGUF): codellama-7b.Q2_K (aliases: codellama-7b-q2-k)
CodeLlama (GGUF): codellama-7b.Q3_K_L (aliases: codellama-7b-q3-k-l)
CodeLlama (GGUF): codellama-7b.Q3_K_M (aliases: codellama-7b-q3-k-m)
CodeLlama (GGUF): codellama-7b.Q3_K_S (aliases: codellama-7b-q3-k-s)
CodeLlama (GGUF): codellama-7b.Q4_K_M (aliases: codellama-7b-q4-k-m)
CodeLlama (GGUF): codellama-7b.Q4_K_S (aliases: codellama-7b-q4-k-s)
CodeLlama (GGUF): codellama-7b.Q5_K_M (aliases: codellama-7b-q5-k-m)
CodeLlama (GGUF): codellama-7b.Q5_K_S (aliases: codellama-7b-q5-k-s)
CodeLlama (GGUF): codellama-7b.Q6_K (aliases: codellama-7b-q6-k)
CodeLlama (GGUF): codellama-7b.Q8_0 (aliases: codellama-7b-q8-0)
CodeLlama (GGUF): codellama-13b.Q2_K (aliases: codellama-13b-q2-k)
CodeLlama (GGUF): codellama-13b.Q3_K_L (aliases: codellama-13b-q3-k-l)
CodeLlama (GGUF): codellama-13b.Q3_K_M (aliases: codellama-13b-q3-k-m)
CodeLlama (GGUF): codellama-13b.Q3_K_S (aliases: codellama-13b-q3-k-s)
CodeLlama (GGUF): codellama-13b.Q4_K_M (aliases: codellama-13b-q4-k-m)
CodeLlama (GGUF): codellama-13b.Q4_K_S (aliases: codellama-13b-q4-k-s)
CodeLlama (GGUF): codellama-13b.Q5_K_M (aliases: codellama-13b-q5-k-m)
CodeLlama (GGUF): codellama-13b.Q5_K_S (aliases: codellama-13b-q5-k-s)
CodeLlama (GGUF): codellama-13b.Q6_K (aliases: codellama-13b-q6-k)
CodeLlama (GGUF): codellama-13b.Q8_0 (aliases: codellama-13b-q8-0)
CodeLlama (GGUF): codellama-34b.Q2_K (aliases: codellama-34b-q2-k)
CodeLlama (GGUF): codellama-34b.Q3_K_L (aliases: codellama-34b-q3-k-l)
CodeLlama (GGUF): codellama-34b.Q3_K_M (aliases: codellama-34b-q3-k-m)
CodeLlama (GGUF): codellama-34b.Q3_K_S (aliases: codellama-34b-q3-k-s)
CodeLlama (GGUF): codellama-34b.Q4_K_M (aliases: codellama-34b-q4-k-m)
CodeLlama (GGUF): codellama-34b.Q4_K_S (aliases: codellama-34b-q4-k-s)
CodeLlama (GGUF): codellama-34b.Q5_K_M (aliases: codellama-34b-q5-k-m)
CodeLlama (GGUF): codellama-34b.Q5_K_S (aliases: codellama-34b-q5-k-s)
CodeLlama (GGUF): codellama-34b.Q6_K (aliases: codellama-34b-q6-k)
CodeLlama (GGUF): codellama-34b.Q8_0 (aliases: codellama-34b-q8-0)
CodeLlama (GGUF): codellama-7b-python.Q2_K (aliases: codellama-7b-python-q2-k)
CodeLlama (GGUF): codellama-7b-python.Q3_K_L (aliases: codellama-7b-python-q3-k-l)
CodeLlama (GGUF): codellama-7b-python.Q3_K_M (aliases: codellama-7b-python-q3-k-m)
CodeLlama (GGUF): codellama-7b-python.Q3_K_S (aliases: codellama-7b-python-q3-k-s)
CodeLlama (GGUF): codellama-7b-python.Q4_K_M (aliases: codellama-7b-python-q4-k-m)
CodeLlama (GGUF): codellama-7b-python.Q4_K_S (aliases: codellama-7b-python-q4-k-s)
CodeLlama (GGUF): codellama-7b-python.Q5_K_M (aliases: codellama-7b-python-q5-k-m)
CodeLlama (GGUF): codellama-7b-python.Q5_K_S (aliases: codellama-7b-python-q5-k-s)
CodeLlama (GGUF): codellama-7b-python.Q6_K (aliases: codellama-7b-python-q6-k)
CodeLlama (GGUF): codellama-7b-python.Q8_0 (aliases: codellama-7b-python-q8-0)
CodeLlama (GGUF): codellama-13b-python.Q2_K (aliases: codellama-13b-python-q2-k)
CodeLlama (GGUF): codellama-13b-python.Q3_K_L (aliases: codellama-13b-python-q3-k-l)
CodeLlama (GGUF): codellama-13b-python.Q3_K_M (aliases: codellama-13b-python-q3-k-m)
CodeLlama (GGUF): codellama-13b-python.Q3_K_S (aliases: codellama-13b-python-q3-k-s)
CodeLlama (GGUF): codellama-13b-python.Q4_K_M (aliases: codellama-13b-python-q4-k-m)
CodeLlama (GGUF): codellama-13b-python.Q4_K_S (aliases: codellama-13b-python-q4-k-s)
CodeLlama (GGUF): codellama-13b-python.Q5_K_M (aliases: codellama-13b-python-q5-k-m)
CodeLlama (GGUF): codellama-13b-python.Q5_K_S (aliases: codellama-13b-python-q5-k-s)
CodeLlama (GGUF): codellama-13b-python.Q6_K (aliases: codellama-13b-python-q6-k)
CodeLlama (GGUF): codellama-13b-python.Q8_0 (aliases: codellama-13b-python-q8-0)
CodeLlama (GGUF): codellama-34b-python.Q2_K (aliases: codellama-34b-python-q2-k)
CodeLlama (GGUF): codellama-34b-python.Q3_K_L (aliases: codellama-34b-python-q3-k-l)
CodeLlama (GGUF): codellama-34b-python.Q3_K_M (aliases: codellama-34b-python-q3-k-m)
CodeLlama (GGUF): codellama-34b-python.Q3_K_S (aliases: codellama-34b-python-q3-k-s)
CodeLlama (GGUF): codellama-34b-python.Q4_K_M (aliases: codellama-34b-python-q4-k-m)
CodeLlama (GGUF): codellama-34b-python.Q4_K_S (aliases: codellama-34b-python-q4-k-s)
CodeLlama (GGUF): codellama-34b-python.Q5_K_M (aliases: codellama-34b-python-q5-k-m)
CodeLlama (GGUF): codellama-34b-python.Q5_K_S (aliases: codellama-34b-python-q5-k-s)
CodeLlama (GGUF): codellama-34b-python.Q6_K (aliases: codellama-34b-python-q6-k)
CodeLlama (GGUF): codellama-34b-python.Q8_0 (aliases: codellama-34b-python-q8-0)
CodeLlama (GGUF): codellama-7b-instruct.Q2_K (aliases: codellama-7b-instruct-q2-k)
CodeLlama (GGUF): codellama-7b-instruct.Q3_K_L (aliases: codellama-7b-instruct-q3-k-l)
CodeLlama (GGUF): codellama-7b-instruct.Q3_K_M (aliases: codellama-7b-instruct-q3-k-m)
CodeLlama (GGUF): codellama-7b-instruct.Q3_K_S (aliases: codellama-7b-instruct-q3-k-s)
CodeLlama (GGUF): codellama-7b-instruct.Q4_K_M (aliases: codellama-7b-instruct-q4-k-m)
CodeLlama (GGUF): codellama-7b-instruct.Q4_K_S (aliases: codellama-7b-instruct-q4-k-s)
CodeLlama (GGUF): codellama-7b-instruct.Q5_K_M (aliases: codellama-7b-instruct-q5-k-m)
CodeLlama (GGUF): codellama-7b-instruct.Q5_K_S (aliases: codellama-7b-instruct-q5-k-s)
CodeLlama (GGUF): codellama-7b-instruct.Q6_K (aliases: codellama-7b-instruct-q6-k)
CodeLlama (GGUF): codellama-7b-instruct.Q8_0 (aliases: codellama-7b-instruct-q8-0)
CodeLlama (GGUF): codellama-13b-instruct.Q2_K (aliases: codellama-13b-instruct-q2-k)
CodeLlama (GGUF): codellama-13b-instruct.Q3_K_L (aliases: codellama-13b-instruct-q3-k-l)
CodeLlama (GGUF): codellama-13b-instruct.Q3_K_M (aliases: codellama-13b-instruct-q3-k-m)
CodeLlama (GGUF): codellama-13b-instruct.Q3_K_S (aliases: codellama-13b-instruct-q3-k-s)
CodeLlama (GGUF): codellama-13b-instruct.Q4_K_M (aliases: codellama-13b-instruct-q4-k-m)
CodeLlama (GGUF): codellama-13b-instruct.Q4_K_S (aliases: codellama-13b-instruct-q4-k-s)
CodeLlama (GGUF): codellama-13b-instruct.Q5_K_M (aliases: codellama-13b-instruct-q5-k-m)
CodeLlama (GGUF): codellama-13b-instruct.Q5_K_S (aliases: codellama-13b-instruct-q5-k-s)
CodeLlama (GGUF): codellama-13b-instruct.Q6_K (aliases: codellama-13b-instruct-q6-k)
CodeLlama (GGUF): codellama-13b-instruct.Q8_0 (aliases: codellama-13b-instruct-q8-0)
CodeLlama (GGUF): codellama-34b-instruct.Q2_K (aliases: codellama-34b-instruct-q2-k)
CodeLlama (GGUF): codellama-34b-instruct.Q3_K_L (aliases: codellama-34b-instruct-q3-k-l)
CodeLlama (GGUF): codellama-34b-instruct.Q3_K_M (aliases: codellama-34b-instruct-q3-k-m)
CodeLlama (GGUF): codellama-34b-instruct.Q3_K_S (aliases: codellama-34b-instruct-q3-k-s)
CodeLlama (GGUF): codellama-34b-instruct.Q4_K_M (aliases: codellama-34b-instruct-q4-k-m)
CodeLlama (GGUF): codellama-34b-instruct.Q4_K_S (aliases: codellama-34b-instruct-q4-k-s)
CodeLlama (GGUF): codellama-34b-instruct.Q5_K_M (aliases: codellama-34b-instruct-q5-k-m)
CodeLlama (GGUF): codellama-34b-instruct.Q5_K_S (aliases: codellama-34b-instruct-q5-k-s)
CodeLlama (GGUF): codellama-34b-instruct.Q6_K (aliases: codellama-34b-instruct-q6-k)
CodeLlama (GGUF): codellama-34b-instruct.Q8_0 (aliases: codellama-34b-instruct-q8-0)
CodeLlama: CodeLlama-7b-hf (aliases: codellama-7b)
CodeLlama: CodeLlama-13b-hf (aliases: codellama-13b)
CodeLlama: CodeLlama-34b-hf (aliases: codellama-34b)
CodeLlama: CodeLlama-7b-Python-hf (aliases: codellama-7b-python)
CodeLlama: CodeLlama-13b-Python-hf (aliases: codellama-13b-python)
CodeLlama: CodeLlama-34b-Python-hf (aliases: codellama-34b-python)
CodeLlama: CodeLlama-7b-Instruct-hf (aliases: codellama-7b-instruct)
CodeLlama: CodeLlama-13b-Instruct-hf (aliases: codellama-13b-instruct)
CodeLlama: CodeLlama-34b-Instruct-hf (aliases: codellama-34b-instruct)
```

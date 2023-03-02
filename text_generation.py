# -*- coding: utf-8 -*-
"""text_generation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yPx4XYgcF8c8yD69RaOn_F8DRErFIg-F
"""

!pip install --quiet gradio

import gradio as gr

title = "GPT-J-6B"

examples = [
    ['The tower is 324 metres (1,063 ft) tall,'],
    ["The Moon's orbit around Earth has"],
    ["The smooth Borealis basin in the Northern Hemisphere covers 40%"]
]

gr.Interface.load("huggingface/EleutherAI/gpt-j-6B", 
    inputs=gr.inputs.Textbox(lines=5, label="Input Text"),
    title=title, examples=examples).launch();
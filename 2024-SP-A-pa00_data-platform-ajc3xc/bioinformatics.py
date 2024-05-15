#!/usr/bin/env python3
# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import skbio  # type: ignore

# %%
with open("jupyter_out.txt", "w") as f:
    print("Hello world", end="", file=f)
    print(skbio.title, end="", file=f)
    print(skbio.art, end="", file=f)

# %%
skbio.title

# %%
skbio.art

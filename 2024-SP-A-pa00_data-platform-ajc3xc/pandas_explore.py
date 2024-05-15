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
import pandas as pd  # type: ignore

# %%
titanic = pd.read_csv("titanic.csv")

titanic.head()

# %%
titanic["Name"].str.lower()

# %%
titanic["Name"].str.split(",")

# %%
titanic["Name"].str.contains("Countess")

# %%

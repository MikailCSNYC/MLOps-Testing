# Databricks notebook source
# adding util folder to the system path
import sys
sys.path.insert(0, '/Workspace/Repos/mikail.krochta@campana-schott.com/MLOps-Testing/util/')
import udf

import pytest
import pandas as pd

# COMMAND ----------

def test_first_two_rows():
    df = pd.DataFrame({"one": [1, 2, 3]})
    x = udf.first_two_rows(df)
    assert x.compare(df[:2]).shape[0] == 0

# COMMAND ----------

def test_shuffle():
    df = pd.DataFrame({"one": [ i for i in range(100)]})
    x = udf.shuffle(df)
    assert x.compare(df).shape[0] != 0

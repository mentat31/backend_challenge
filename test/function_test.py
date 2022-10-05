from src.functions import date_filter as df, extract as e, hash_count as hc
import pandas as pd

def test_ret():
    assert len(e.retrieve_data("resources/decodes.json")) == 10000

def test_key():
    assert len(e.retrieve_data_key("resources/encodes.csv")) == 6

def test_time():
    data = pd.read_json("resources/decodes.json")
    d = df.date_parse(data, [2021])
    d2 = [i.year == 2021 for i in d['timestamp']]
    assert all(d) == True

def test_index():
    data = pd.read_json("resources/decodes.json")
    k = e.retrieve_data_key("resources/encodes.csv")
    d = df.date_parse(data, [2021])
    fin = hc.clean_index(d, k)
    h = sorted(list(k['hash']))
    assert sorted(list(fin.index)) == h

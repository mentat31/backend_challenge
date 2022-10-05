import pandas as pd


def clean_index(data, key) -> pd.Series:

    """
    Function to filter out bitlinks not in data key. First, splitting the bitlink string on '/'
    to isolate the hash and domain fields. Elements in domain_field are filtered using the domain key, removing
    those not recognized. This new index is then filtered by the hash field, leaving only those
    found in the hash key. The function finally returns a value count of the hashes. Array like,
    indexed by the hash, with elements being the count for each hash.


    :param data: data returned from clean_time
    :param key: the data_key returned from retrieve_data_key
    :return: value counts indexed by hash
    """

    hash_field = data.bitlink.apply(lambda x: x.split("/")[-1])
    domain_field = data.bitlink.apply(lambda x: x.split("/")[-2])

    prot = data.bitlink.apply(lambda x: x.split("/")[0])

    hash_keys = list(key.hash)
    domain_keys = list(key.domain)

    domain_index = domain_field[domain_field.apply(lambda x: x in domain_keys).index]
    hash_index = domain_index[hash_field.apply(lambda x: x in hash_keys)].index

    return hash_field[hash_index].value_counts()


if __name__ == "__main__":

    from date_filter import *

    df = pd.read_json("../../resources/decodes.json")
    k = pd.read_csv("../../resources/encodes.csv")

    t1 = date_clean(df, 2021)

    print(clean_index(t1, k))

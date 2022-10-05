import pandas as pd


def retrieve_data(path: [str | bytes]) -> pd.DataFrame:
    """
    Retrieve data to be wrangled. The Pandas library was selected
    in order to utilize some key features.

    1) Consistency with other read method
    2) Context automatically managed (open/close)
    3) Source can be .json file or a valid JSON string if calling an API.

    :param: path: Data source.
    :return: Pandas Dataframe.
    """

    get = pd.read_json(path)
    return get


def retrieve_data_key(path: str) -> pd.DataFrame:
    """
    Retrieve metadata for context. This function automatically reads a csv, given
    the nature of the challenge. However, if querying a Database, the returned query could be mapped
    to a similar object/struct.

    :param: path: Metadata source
    :return: Pandas dataframe.
    """
    key = pd.read_csv(path)
    return key

if __name__ == "__main__":
    t1 = retrieve_data("../../resources/decodes.json")
    print("retrieved : ", len(t1))

    t2 = retrieve_data_key("../../resources/encodes.csv")
    print("key retrieved : ", len(t2))


from functions import date_filter as df, extract as e, hash_count as hc
import json


def main(data: str, key: str, date: list[int]):

    """

    :param data: path or file like object
    :param key: reference key for data
    :param date: desired date range in form of [Year,Month,Day]
    :return:
    """

    click_data = e.retrieve_data(data)
    data_key = e.retrieve_data_key(key)

    time_filtered = df.date_parse(click_data, date)
    key_filter = hc.clean_index(time_filtered, data_key)

    # Dictionary (or hash map) with hash:url pair
    long_hash = {v['hash']: v['long_url'] for v in data_key.to_dict(orient="records")}

    final = []

    for click in key_filter.index:

        click_count = dict([(long_hash[click], int(key_filter[click]))])

        final.append(click_count)

    return json.dumps(final)


if __name__ == "__main__":

    source = "resources/decodes.json"
    ref_key = "resources/encodes.csv"
    year = [2021]

    print(main(source, ref_key, year))

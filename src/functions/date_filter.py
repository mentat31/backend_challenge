import pandas as pd


def date_clean(data: pd.DataFrame, target_year: int, **kwargs) -> pd.DataFrame:
    """
    Function for filtering date criteria. Requires target_year, however
    If additional granularity is needed, months and/or days can be passed as keyword arguments
    ex: date_clean(data, 2022, month = 3, day = 31)

    :param data: Response from retrieve_data.py.
    :param target_year: Desired year.
    :param kwargs: If additional granularity is needed, months and days can be passed as integers.
    :return: Dataframe with specified date.
    """
    if kwargs:

        target_month = kwargs.get("month", None)
        target_day = kwargs.get('day', None)

        clean_year = data[data.timestamp.apply(lambda x: x.year == target_year)]
        clean_month = clean_year[clean_year.timestamp.apply(lambda x: x.month == target_month)]

        if target_day:

            clean_day = clean_month[clean_month.timestamp.apply(lambda x: x.day == target_day)]

            return clean_day

        else:

            return clean_month

    else:

        cleaned = data[data.timestamp.apply(lambda x: x.year == target_year)]
        return cleaned


def date_parse(data, date: list[int]) -> pd.DataFrame:

    """
    Higher Order Function for date granularity.

    :param data: data returned from retrieve_data
    :param date: list of int representing [Year, Month, Day]
    :return: dataset with desired date range
    """

    if len(date) == 0 or len(date) > 3:
        print("Please enter a valid date")
        return 1

    elif len(date) == 1:
        return date_clean(data, date[0])

    elif len(date) == 2:
        return date_clean(data, date[0], month=date[1])

    else:
        return date_clean(data, date[0], month=date[1], day=date[2])


if __name__ == "__main__":

    df = pd.read_json("../../resources/decodes.json")

    print(date_parse(df, [2021])['timestamp'].head())

    print(date_parse(df, [2021, 3])['timestamp'].head())

    print(date_parse(df, [2021, 3, 31])['timestamp'].head())



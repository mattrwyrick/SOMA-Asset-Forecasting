import os
import datetime
import pandas as pd

from soma_forecasts.settings import (
    DATA_DIRECTORY,
    MARKETS_BASE_URL,
    SOMA_MBS_API,
    SOMA_MBS_END_DATE,
    SOMA_MBS_START_DATE,
    ROOT_DIRECTORY
)


EXTENSION = "csv"
NEW_FILE_BASE_NAME = "soma-agency-mbs-"
TIME_DELTA = datetime.timedelta(days=7)


def download():
    """
    Download the data to the data directory
    :return:
    """
    agg_data = list()
    current_mbs_date = SOMA_MBS_START_DATE
    while current_mbs_date != SOMA_MBS_END_DATE:

        df = load_data(current_mbs_date)
        total = df['Current Face Value'].sum()
        agg_data.append([current_mbs_date, total])

        current_dt = api_string_to_datetime(current_mbs_date)
        next_dt = current_dt + TIME_DELTA
        current_mbs_date = datetime_to_api_string(next_dt)

    write_aggregate(agg_data)


def write_aggregate(agg_data):
    """
    Write the aggregate data to the root directory
    :param agg_data:
    :return:
    """
    path = os.path.join(ROOT_DIRECTORY, "aggregate_agency_mbs.csv")
    df = pd.DataFrame(agg_data, columns=["Date", "Current Face Value"])
    df.replace(to_replace=0, method='ffill', inplace=True)  # few instances where dates note released on wednesday - adjust zeros
    with open(path, "w+") as f:
        df.to_csv(f)


def load_data(dt_string):
    """
    Save the data from the response
    :param response:
    :param dt_string:
    :return:
    """
    name = NEW_FILE_BASE_NAME + dt_string + "." + EXTENSION
    path = os.path.join(DATA_DIRECTORY, name)
    with open(path, mode="r", encoding="utf-8")as f:
        df = pd.read_csv(f)
    return df


def datetime_to_api_string(dt):
    """
    Convert the
    :param dt:
    :return:
    """
    dt_string = dt.strftime("%Y-%m-%d")
    return dt_string


def api_string_to_datetime(dt_string):
    """
    Convert an api string to a datetime object
    :param dt_string:
    :return:
    """
    dt = datetime.datetime.strptime(dt_string, "%Y-%m-%d")
    return dt


if __name__ == "__main__":
    download()


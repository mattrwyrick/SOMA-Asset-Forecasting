import os
import requests
import datetime

from soma_forecasts.settings import (
    DATA_DIRECTORY,
    MARKETS_BASE_URL,
    SOMA_MBS_API,
    SOMA_MBS_END_DATE,
    SOMA_MBS_START_DATE
)


SOMA_MBS_BASE_URL = MARKETS_BASE_URL + SOMA_MBS_API
EXTENSION = "csv"
DOWNLOADED_FILE_NAME = "details." + EXTENSION
NEW_FILE_BASE_NAME = "soma-agency-mbs-"
TIME_DELTA = datetime.timedelta(days=7)


def download():
    """
    Download the data to the data directory
    :return:
    """

    current_mbs_date = SOMA_MBS_START_DATE
    while current_mbs_date != SOMA_MBS_END_DATE:

        url = SOMA_MBS_BASE_URL + current_mbs_date + "." + EXTENSION
        response = requests.get(url)
        save_data(response, current_mbs_date)
        current_dt = api_string_to_datetime(current_mbs_date)
        next_dt = current_dt + TIME_DELTA
        current_mbs_date = datetime_to_api_string(next_dt)


def save_data(response, dt_string):
    """
    Save the data from the response
    :param response:
    :param dt_string:
    :return:
    """
    encoding = response.encoding
    name = NEW_FILE_BASE_NAME + dt_string + "." + EXTENSION
    path = os.path.join(DATA_DIRECTORY, name)
    with open(path, mode="wb+") as f:
        f.write(response.content)


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


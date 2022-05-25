import os
import pandas as pd

from soma_forecasts.settings import ROOT_DIRECTORY


def load_aggregate():
    """
    Loadd the full aggregate file
    :return:
    """
    path = os.path.join(ROOT_DIRECTORY, "aggregate_agency_mbs.csv")
    with open(path, "r") as f:
        df = pd.read_csv(f)

    df['Date'] = df['Date'].astype('datetime64[ns]')
    df.set_index('Date')
    df.sort_index(inplace=True)
    return df







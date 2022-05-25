import os
from pathlib import Path


APP_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
SRC_DIRECTORY = Path(APP_DIRECTORY).parent
ROOT_DIRECTORY = Path(SRC_DIRECTORY).parent
DATA_DIRECTORY = os.path.join(ROOT_DIRECTORY, "data")


MARKETS_BASE_URL = "https://markets.newyorkfed.org/api/"


SOMA_MBS_API = "soma/agency/get/mbs/asof/"  # include [DATE].[FORMAT]  e.g. 2020-10-21.xml
SOMA_MBS_START_DATE = "2012-05-16"
SOMA_MBS_END_DATE = "2022-05-18"




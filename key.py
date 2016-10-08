# coding: UTF-8

import os
import os.path

import dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
dotenv.load_dotenv(dotenv_path)

CK = os.environ.get("CONSUMER_KEY")
CS = os.environ.get("CONSUMER_SECRET")
AK = os.environ.get("ACCESS_TOKEN_KEY")
AS = os.environ.get("ACCESS_TOKEN_SECRET")


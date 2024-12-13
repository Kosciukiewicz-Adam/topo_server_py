from dotenv import load_dotenv, find_dotenv
import os
load_dotenv(find_dotenv())
mongo_passwd = os.environ.get("MONGODB_PASSWD")
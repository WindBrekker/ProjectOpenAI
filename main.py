#Packages
import os
from os import getenv

import openai
import logging
from dotenv import load_dotenv

####
logging.basicConfig(level=logging.INFO, filename="logs.log",
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.info("-------------------------------------------------Program started")

load_dotenv()


####  Read Key
try:
    openai.api_key = os.getenv("OPENAI_KEY")
except:
    logging.error("OpenAI API key not found in environment variables")
else:
    logging.info("OpenAI API key set")
    logging.info(openai.api_key)
    print(getenv("OPENAI_KEY"))



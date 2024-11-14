#Packages
import os
import sys
import openai
import logging
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv
import utils

import utils

#### Set configuration of logs and files
prompt = "prompt.txt"
article = "article.txt"
logging_file = "logs.log"

rfhandler = RotatingFileHandler(
    logging_file,
    mode="a",
    maxBytes=4096,
    backupCount=1
)
logging.basicConfig(level=logging.INFO,
                    handlers=[rfhandler],
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
####
####

logging.info("-------------------------------------------------Program started")
load_dotenv()


#### Read Key from .env file
try:
    openai_api_key = os.getenv("OPENAI_KEY")
except:
    logging.error("OpenAI API key not found in environment variables")
    sys.exit()
else:
    logging.info("OpenAI API key set")


#### Get response from OpenAI chatbot
response = str(utils.send_to_chatbot(openai_api_key, prompt, article))

#Save output to file
with open("artykul.html", "w", encoding="utf-8") as file:
    file.write(response)
logging.info("Response saved to artykul.html")

logging.info("-------------------------------------------------Program finished")





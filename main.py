#Packages
import os
import sys
import openai
import logging
from dotenv import load_dotenv
import utils

import utils

#### Set configuration of logs and files
prompt = "prompt.txt"
article = "article.txt"
logging_file = "logs.log"

logging.basicConfig(level=logging.INFO, filename=logging_file,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
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
response = utils.send_to_chatbot(openai_api_key, prompt, article)





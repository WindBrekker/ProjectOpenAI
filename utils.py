import openai
import logging
import sys

def read_file(filename):
    try:
        file_with_text = open(filename, 'r')
    except FileNotFoundError:
        logging.error(f"Cannot find file: {filename}")
        sys.exit()
        return None
    else:
        logging.info(f"Read file {filename}")
        return file_with_text.read()


def send_to_chatbot(key, prompt_file, article_file):
    """The function is supposed to combine prompt and given article.
    Then return chatbot's answer in form of .html file using openai.Completion.create() function."""

    prompt_text = read_file(prompt_file)
    article_text = read_file(article_file)

    full_prompt = prompt_text + "\n\n\n\n" + article_text
    
    try:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",
            prompt=full_prompt,
            max_tokens=100
        )
    except Exception as e:
        logging.error(f"Error while sending prompt to OpenAI: {e}")
        sys.exit()
    else:
        logging.info("Prompt sent successfully. Await response.")
        return response.choices[0].text



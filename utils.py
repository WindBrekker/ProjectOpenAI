import openai
import logging

def read_file(filename):
    try:
        file_with_text = open(filename, 'r')
    except FileNotFoundError:
        logging.error(f"Cannot find file: {filename}")
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


    return full_prompt


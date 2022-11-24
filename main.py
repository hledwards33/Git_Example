import logging

from models.english_models.say_hello import Hello
from models.english_models.say_goodbye import Goodbye

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def run_model(name: str, language: str):
    if language == "English":
        Hello.run(name)
        print("Do something...")
        Goodbye.run(name)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    logger.info("Model has started to run.")
    run_model(name="Credit Risk", language="English")
    logger.info("Model has finished running.")

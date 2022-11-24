import logging

from models.english_models.say_hello import Hello
from models.english_models.say_goodbye import Goodbye
from models.spanish_models.decir_hola import Hola
from models.spanish_models.decir_adios import Adios

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def run_model(name: str, language: str):
    if language == "English":
        hello = Hello(name=name)
        hello.run()
        print("Do something...")
        goodbye = Goodbye(name=name)
        goodbye.run()
    if language == "Spanish":
        hola = Hola(name=name)
        hola.run()
        print("Hacer Algo...")
        adios = Adios(name=name)
        adios.run()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_model(name="Credit Risk", language="Spanish")
    logger.info("Model has finished running.")

from models.base_model import BaseModel


class Goodbye(BaseModel):

    def __init__(self):
        pass

    def run(self, name: str):
        print(f"Goodbye {name}")

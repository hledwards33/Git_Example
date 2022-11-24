from models.base_model import BaseModel


class Hello(BaseModel):

    def __init__(self):
        pass

    def run(self, name: str):
        print(f"Hello {name}")

from models.base_model import BaseModel


class Hola(BaseModel):

    def __init__(self, name: str):
        super().__init__(name=name)

    def run(self):
        print(f"Hola {self.name}")

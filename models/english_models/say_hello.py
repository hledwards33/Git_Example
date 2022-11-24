from models.base_model import BaseModel


class Hello(BaseModel):

    def __init__(self, name: str):
        super().__init__(name=name)

    def run(self):
        print(f"Hello {self.name}")

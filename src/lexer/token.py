class Token:
    def __init__(self, type: str, value: str, pos: tuple) -> None:
        self.type = type
        self.value = value
        self.ln, self.col = pos
    def value(self):
        print(self.value)
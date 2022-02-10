

class TwelveDivisionError(Exception):
    def __init__(self) -> None:
        super().__init__("Division par 12 !")


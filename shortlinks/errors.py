class NotUniqueKey(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class KeyGenerationError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

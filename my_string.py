class MyString:
    def __init__(self, string: str):
        self.__string = string

    def get_string(self) -> str:
        return self.__string

    def set_string(self, string: str):
        self.__string = string

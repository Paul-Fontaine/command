from my_string import MyString
from abc import ABC, abstractmethod


class Command(ABC):
    def __init__(self, my_string: MyString):
        self._my_string = my_string

    @abstractmethod
    def execute(self):
        raise NotImplementedError

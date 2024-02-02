from typing import Dict
from command import Command


class StringCommandInvoker:
    def __init__(self):
        self.__commands: Dict[str: Command] = {}

    def add_command(self, name: str, command: Command):
        self.__commands[name] = command

    def invoke_command(self, name: str):
        self.__commands[name].execute()

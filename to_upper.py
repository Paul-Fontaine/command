from overrides import override
from command import Command, MyString


class ToUpper(Command):
    def __init__(self, my_string: MyString):
        Command.__init__(self, my_string)

    @override
    def execute(self):
        self._my_string.set_string(self._my_string.get_string().upper())

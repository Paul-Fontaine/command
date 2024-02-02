from overrides import override
from command import Command, MyString


class ToLower(Command):
    def __init__(self, my_string: MyString):
        Command.__init__(self, my_string)

    @override
    def execute(self):
        self._my_string.set_string(self._my_string.get_string().lower())


class ToUpper(Command):
    def __init__(self, my_string: MyString):
        Command.__init__(self, my_string)

    @override
    def execute(self):
        self._my_string.set_string(self._my_string.get_string().upper())


class Simplify(Command):
    def __init__(self, my_string: MyString):
        Command.__init__(self, my_string)

    @override
    def execute(self):
        self._my_string.set_string(self._my_string.get_string().replace(' ', ''))


class Reverse(Command):
    def __init__(self, my_string: MyString):
        Command.__init__(self, my_string)

    @override
    def execute(self):
        self._my_string.set_string(self._my_string.get_string()[::-1])


class TeTe(Command):
    def __init__(self, my_string: MyString):
        Command.__init__(self, my_string)

    @override
    def execute(self):
        self._my_string.set_string(''.join([char.upper() if index % 2 == 0 else char for index, char in enumerate(self._my_string.get_string())]))

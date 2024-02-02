from PySide6.QtWidgets import QWidget, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout
from command_string_invoker import StringCommandInvoker
from commands import ToLower, ToUpper, Simplify, Reverse, TeTe
from my_string import MyString


class StringCommandWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.__my_string: MyString = MyString("")

        self.__invoker: StringCommandInvoker = StringCommandInvoker()
        self.__add_commands_to_invoker()

        self.add_widgets()

        self.set_layout()

    def __add_commands_to_invoker(self):
        tolower = ToLower(self.__my_string)
        self.__invoker.add_command('to lower', tolower)

        toupper = ToUpper(self.__my_string)
        self.__invoker.add_command('to upper', toupper)

        reverse = Reverse(self.__my_string)
        self.__invoker.add_command('reverse', reverse)

        simplify = Simplify(self.__my_string)
        self.__invoker.add_command('simplify', simplify)

        tete = TeTe(self.__my_string)
        self.__invoker.add_command('tete', tete)

    def add_widgets(self):
        self.__line_edit: QLineEdit = QLineEdit(self)
        self.__line_edit.setPlaceholderText('type here ...')

        self.__button_lower: QPushButton = QPushButton('lower case', self)
        self.__button_lower.clicked.connect(self.__invoke_lower_case_command)

        self.__button_upper: QPushButton = QPushButton('upper case', self)
        self.__button_upper.clicked.connect(self.__invoke_upper_case_command)

        self.__button_simplify: QPushButton = QPushButton('simplify', self)
        self.__button_simplify.clicked.connect(self.__invoke_simplify_command)

        self.__button_reverse: QPushButton = QPushButton('reverse', self)
        self.__button_reverse.clicked.connect(self.__invoke_reverse_command)

        self.__button_tete: QPushButton = QPushButton('TeTe', self)
        self.__button_tete.clicked.connect(self.__invoke_tete_command)

    def set_layout(self):
        vlayout = QVBoxLayout(self)
        hlayout1 = QHBoxLayout(self)
        hlayout2 = QHBoxLayout(self)

        hlayout1.addWidget(self.__line_edit)

        hlayout2.addWidget(self.__button_lower)
        hlayout2.addWidget(self.__button_upper)
        hlayout2.addWidget(self.__button_simplify)
        hlayout2.addWidget(self.__button_reverse)
        hlayout2.addWidget(self.__button_tete)

        vlayout.addLayout(hlayout1)
        vlayout.addLayout(hlayout2)

    def __invoke_lower_case_command(self):
        self.__my_string.set_string(self.__line_edit.text())
        self.__invoker.invoke_command('to lower')
        self.__line_edit.setText(self.__my_string.get_string())

    def __invoke_upper_case_command(self):
        self.__my_string.set_string(self.__line_edit.text())
        self.__invoker.invoke_command('to upper')
        self.__line_edit.setText(self.__my_string.get_string())

    def __invoke_simplify_command(self):
        self.__my_string.set_string(self.__line_edit.text())
        self.__invoker.invoke_command('simplify')
        self.__line_edit.setText(self.__my_string.get_string())

    def __invoke_reverse_command(self):
        self.__my_string.set_string(self.__line_edit.text())
        self.__invoker.invoke_command('reverse')
        self.__line_edit.setText(self.__my_string.get_string())

    def __invoke_tete_command(self):
        self.__my_string.set_string(self.__line_edit.text())
        self.__invoker.invoke_command('tete')
        self.__line_edit.setText(self.__my_string.get_string())

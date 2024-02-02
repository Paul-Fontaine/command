import sys
from PySide6.QtWidgets import QApplication
from string_commands_window import StringCommandWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = StringCommandWindow()
    window.show()

    sys.exit(app.exec())

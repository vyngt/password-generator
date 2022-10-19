import functools
from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QTextEdit,
    QCheckBox,
    QApplication,
    QSpinBox,
    QVBoxLayout,
    QHBoxLayout,
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt


from core import gen_password

__all__ = ["MainWindow"]

PASSWORD_SETTING = ("Lowercase", "Uppercase", "Digit", "Special")


class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initialize()

    def initialize(self):
        self.initialize_settings_data()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(300, 100, 300, 250)
        self.setWindowTitle("Password Generator")
        self.setup_main_window()
        self.show()

    def initialize_settings_data(self):
        self.__size = 1
        self.__cbox = [True, True, True, True]

    def get_settings_data(self) -> tuple[int, bool, bool, bool, bool]:
        "Length, Upper, Lower, Digit, Special"
        return self.__size, *self.__cbox

    def setup_main_window(self):
        header = QLabel("Password Generator")
        header.setFont(QFont("Arial", 20))
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)

        setting_label = QLabel("Setting")
        setting_label.setFont(QFont("Arial", 14))

        vbox = QVBoxLayout(self)
        vbox.addWidget(header)
        vbox.addWidget(setting_label)

        size_setting_layout = QHBoxLayout()
        letter_settings_layout = QHBoxLayout()
        btn_layout = QHBoxLayout()

        self.setup_size_setting_interface(size_setting_layout)
        self.setup_settings_interface(letter_settings_layout)
        self.setup_btn_interface(btn_layout)

        self.password_output = QTextEdit()

        vbox.addLayout(size_setting_layout)
        vbox.addLayout(letter_settings_layout)
        vbox.addLayout(btn_layout)
        vbox.addWidget(self.password_output)

    def setup_btn_interface(self, hbox: QHBoxLayout):
        def generate():
            self.password_output.setPlainText(gen_password(*self.get_settings_data()))

        def copy():
            QApplication.clipboard().setText(self.password_output.toPlainText())

        generate_btn = QPushButton("Generate")
        generate_btn.clicked.connect(generate)

        copy_btn = QPushButton("Copy")
        copy_btn.clicked.connect(copy)

        hbox.addWidget(generate_btn)
        hbox.addWidget(copy_btn)

    def setup_size_setting_interface(self, hbox: QHBoxLayout):
        def handle_changed(value: int):
            self.__size = value

        size_label = QLabel("Size")
        size_spin = QSpinBox()
        size_spin.setRange(1, 150)
        size_spin.setValue(1)
        size_spin.valueChanged.connect(handle_changed)

        hbox.addWidget(size_label)
        hbox.addWidget(size_spin)

    def setup_settings_interface(self, hbox: QHBoxLayout):
        def handle_toggle(idx: int, checked: bool):
            self.__cbox[idx] = checked

        for i, name in enumerate(PASSWORD_SETTING):
            cb = QCheckBox(name)
            cb.setChecked(self.__cbox[i])
            cb.toggled.connect(functools.partial(handle_toggle, i))
            hbox.addWidget(cb)

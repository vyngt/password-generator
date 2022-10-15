from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QCheckBox,
    QApplication,
)
from PyQt6.QtGui import QIntValidator
from PyQt6.QtCore import Qt
from .pgen import gen_password

__all__ = ["MainWindow"]


class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(300, 100, 300, 250)
        self.setWindowTitle("Password Generator")
        self.setup_main_window()
        self.show()

    def setup_main_window(self):
        self.name_label = QLabel("Settings:", self)
        self.name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.name_label.move(30, 10)

        self.setup_settings_interface()

        self.button = QPushButton("Generate", self)
        self.button.move(70, 210)
        self.button.clicked.connect(self.generate_password)

        self.pw_zone = QLineEdit(self)
        self.pw_zone.setText("Password")
        self.pw_zone.move(70, 180)

        self.copy_btn = QPushButton("Copy", self)
        self.copy_btn.move(150, 210)
        self.copy_btn.clicked.connect(self.copy_password)

    def copy_password(self):
        QApplication.clipboard().setText(self.pw_zone.text())

    def setup_settings_interface(self):
        self.password_size_label = QLabel("Length:", self)
        self.password_size_label.move(40, 30)
        self.length_edit = QLineEdit("12", self)
        self.length_edit.setValidator(QIntValidator(1, 50))
        self.length_edit.move(120, 30)
        self.lower_cb = QCheckBox("Lowercase", self)
        self.lower_cb.setChecked(True)
        self.lower_cb.move(40, 60)
        self.upper_cb = QCheckBox("Uppercase", self)
        self.upper_cb.setChecked(True)
        self.upper_cb.move(120, 60)
        self.digit_cb = QCheckBox("Digit", self)
        self.digit_cb.setChecked(True)
        self.digit_cb.move(40, 90)
        self.special_cb = QCheckBox("Special", self)
        self.special_cb.setChecked(True)
        self.special_cb.move(120, 90)

    def get_settings(self):
        l = self.length_edit.text()
        length = int(l) if l else 0
        lower = self.lower_cb.isChecked()
        upper = self.upper_cb.isChecked()
        digit = self.digit_cb.isChecked()
        special = self.special_cb.isChecked()

        return length, lower, upper, digit, special

    def generate_password(self):
        self.pw_zone.setText(gen_password(*self.get_settings()))

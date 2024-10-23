# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QInputDialog, QDialog, QVBoxLayout, QLineEdit, QPushButton
from PySide6.QtCore import Qt
import re
import requests
import unittest

PASSWORD_REGEX = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"

def is_strong_password(password) -> bool:
    return bool(re.match(PASSWORD_REGEX, password))

def check_passwords_from_file(file_path):
    results_good = []
    try:
        with open(file_path, 'r') as file:
            passwords = file.readlines()
            for password in passwords:
                password = password.strip()
                if is_strong_password(password):
                    print(f"Good password: {password}")
                    results_good.append((password, True))
                else:
                    print(f"Invalid password: {password}")
    except Exception as e:
        print(f"Ошибка открытия файла: {str(e)}")
    return results_good

def showInf():
    print("1. Проверить пароль")
    print("2. Проверить пароли из файла")
    print("3. Unit тестирование")
    print("4. Выход")


class FileDropWidget(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Выбор файла")
        self.setAcceptDrops(True)

        self.layout = QVBoxLayout(self)

        # Поле для отображения пути файла
        self.file_path_edit = QLineEdit(self)
        self.file_path_edit.setPlaceholderText("Перетащите сюда файл или введите путь вручную")
        self.layout.addWidget(self.file_path_edit)

        # Кнопка для подтверждения выбора файла
        self.confirm_button = QPushButton("Подтвердить файл", self)
        self.confirm_button.clicked.connect(self.accept)
        self.layout.addWidget(self.confirm_button)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        urls = event.mimeData().urls()
        if urls:
            # Получаем путь к файлу
            file_path = urls[0].toLocalFile()
            self.file_path_edit.setText(file_path)

    def get_file_path(self):
        return self.file_path_edit.text()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    while True:
        showInf()

        method, ok = QInputDialog.getInt(None, "Выбор метода", "Введите номер метода: ")
        if ok:
            if method == 1:
                password, ok = QInputDialog.getText(None, "Проверка пароля", "Введите пароль для проверки:")
                if ok and password:
                    if is_strong_password(password):
                        print("Good password")
                    else:
                        print("Invalid password")
            elif method == 2:
            elif method == 3:
                print("Unit тестирование")
                # Место для кода юнит тестов

            elif method == 4:
                print("Выход")
                exit()
            else:
                print("Нет такого метода работы")

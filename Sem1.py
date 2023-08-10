# Задание №1
# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания
# (time.time)
#
# 2.Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.

import datetime

class MyString(str):
    """
    Класс MyString, наследующий от встроенного класса str.
    Добавляет атрибуты autor и time_create к строковому объекту.

    Параметры:
    - current_str (str): Исходная строка.
    - autor (str): Автор строки.

    Атрибуты:
    - autor (str): Автор строки.
    - time_create (datetime.datetime): Время создания объекта.

    Методы:
    - display_info(): Выводит информацию об объекте на печать.
    """

    def __new__(cls, current_str, autor):
        instance = super().__new__(cls, current_str)
        instance.autor = autor
        instance.time_create = datetime.datetime.today()
        return instance

    def display_info(self):
        """
        Выводит информацию об объекте на печать.
        """
        print(f"Строка: {self}")
        print(f"Автор: {self.autor}")
        print(f"Время создания: {self.time_create}")


# Создание экземпляра класса MyString
spam = MyString('чудный день', 'сурок')

# Вывод информации об объекте
spam.display_info()


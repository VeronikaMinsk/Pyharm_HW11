# Задание №4
# Доработаем класс Архив из задачи 2.
# Добавьте методы представления экземпляра для программиста
# и для пользователя.
#
# 2.Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.

class Arhiv:
    """
    Класс Arhiv представляет собой архив синглтона, который хранит информацию о тексте и номере.

    Attributes:
        _instance (Arhiv): Единственный экземпляр класса Arhiv.
        list_arhiv (list): Список экземпляров класса Arhiv.

    Methods:
        __new__(cls, *args, **kwargs): Создает или возвращает существующий экземпляр класса Arhiv.
        __init__(self, text: str, number: int): Инициализирует атрибуты текста и номера.
        __str__(self): Возвращает строковое представление экземпляра.
        __repr__(self): Возвращает строку, представляющую экземпляр для воссоздания.
        print_info(self): Выводит информацию о тексте и номере на печать.
    """

    _instance = None
    list_arhiv = []

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.list_arhiv = []

        cls._instance.list_arhiv.append(cls._instance)

        return cls._instance

    def __init__(self, text: str, number: int):
        """
        Инициализирует экземпляр класса Arhiv.

        Args:
            text (str): Текстовая информация.
            number (int): Номер.

        Returns:
            None
        """
        self.text = text
        self.number = number

    def __str__(self):
        """
        Возвращает строковое представление экземпляра.

        Returns:
            str: Строковое представление.
        """
        return f'Текущий текст строки: {self.text}, число строки: {self.number}'

    def __repr__(self):
        """
        Возвращает строку, представляющую экземпляр для воссоздания.

        Returns:
            str: Строка для воссоздания.
        """
        return f'Arhiv("{self.text}", {self.number})'

    def print_info(self):
        """
        Выводит информацию о тексте и номере на печать.

        Returns:
            None
        """
        print(f'Текущий текст строки: {self.text}, число строки: {self.number}')

# Создаем экземпляры класса Arhiv
spam = Arhiv("ночной страж", 65)
spam3 = Arhiv("дневной дозор", 1555)

# Выводим информацию о созданных экземплярах
print(spam)
print(spam3)

# Выводим атрибуты напрямую
print(f'{spam.text =}, {spam.number =}')

# Выводим список экземпляров
print(f'Список архивов: {Arhiv.list_arhiv}')

# Проверяем метод __repr__ для создания экземпляра класса из строки
evaluated_spam = eval(repr(spam))
print(evaluated_spam)





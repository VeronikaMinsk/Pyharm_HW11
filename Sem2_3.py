# Задание №2
# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списковархивов
# list-архивы также являются свойствами экземпляра
#
# Задание №3
# Добавьте к задачам 1 и 2 строки документации для классов.
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
        print_info(self): Выводит информацию о тексте и номере на печать.
    """

    _instance = None
    list_arhiv = []

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.list_arhiv = []

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
        self.list_arhiv.append(self)

    def print_info(self):
        """
        Выводит информацию о тексте и номере на печать.

        Returns:
            None
        """
        print(f'Text: {self.text}, Number: {self.number}')

# Создаем экземпляры класса Arhiv
spam = Arhiv("ночной страж", 65)
spam3 = Arhiv("дневной дозор", 1555)

# Выводим информацию о созданных экземплярах
spam.print_info()
spam3.print_info()

# Выводим список экземпляров
print(f'List of Arhiv instances: {Arhiv.list_arhiv}')

# Выводим документацию класса Arhiv
help(Arhiv)

# Задание №5
# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр
# прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.
#
# Задание №6
# Доработайте прошлую задачу.
# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения
#
# 2.Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.



class Rectangle:
    """
    Класс Rectangle представляет прямоугольник с заданными высотой и шириной (по умолчанию квадрат).

    Attributes:
        height (int): Высота прямоугольника.
        width (int): Ширина прямоугольника (по умолчанию равна высоте).

    Methods:
        get_perimeter(self): Вычисляет периметр прямоугольника.
        get_area(self): Вычисляет площадь прямоугольника.
        __add__(self, other): Выполняет операцию сложения для создания нового прямоугольника.
        __sub__(self, other): Выполняет операцию вычитания для создания нового прямоугольника.
        __eq__(self, other): Проверяет, равны ли площади двух прямоугольников.
        __ne__(self, other): Проверяет, различны ли площади двух прямоугольников.
        __lt__(self, other): Проверяет, является ли площадь текущего прямоугольника меньше площади другого.
        __le__(self, other): Проверяет, является ли площадь текущего прямоугольника меньше или равной площади другого.
        __gt__(self, other): Проверяет, является ли площадь текущего прямоугольника больше площади другого.
        __ge__(self, other): Проверяет, является ли площадь текущего прямоугольника больше или равной площади другого.
        __str__(self): Возвращает строковое представление прямоугольника.
    """

    def __init__(self, height: int, width=None):
        """
        Инициализирует экземпляр класса Rectangle.

        Args:
            height (int): Высота прямоугольника.
            width (int): Ширина прямоугольника (по умолчанию равна высоте).

        Returns:
            None
        """
        self.height = height
        if width is None:
            self.width = height
        else:
            self.width = width

    def get_perimeter(self):
        """
        Вычисляет периметр прямоугольника.

        Returns:
            int: Периметр прямоугольника.
        """
        return 2 * (self.height + self.width)

    def get_area(self):
        """
        Вычисляет площадь прямоугольника.

        Returns:
            int: Площадь прямоугольника.
        """
        return self.width * self.height

    def __add__(self, other):
        if isinstance(other, Rectangle):
            perimeter = self.get_perimeter() + other.get_perimeter()
            side_a = perimeter // 6
            side_b = (perimeter - side_a * 2) // 2
            return Rectangle(side_a, side_b)
        else:
            raise ValueError("Unsupported operand type for +")

    def __sub__(self, other):
        if isinstance(other, Rectangle):
            perimeter = abs(self.get_perimeter() - other.get_perimeter())
            side_a = perimeter // 6
            side_b = (perimeter - side_a * 2) // 2
            return Rectangle(side_a, side_b)
        else:
            raise ValueError("Unsupported operand type for -")

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.get_area() == other.get_area()
        return False

    def __ne__(self, other):
        if isinstance(other, Rectangle):
            return self.get_area() != other.get_area()
        return True

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.get_area() < other.get_area()
        raise ValueError("Unsupported operand type for <")

    def __le__(self, other):
        if isinstance(other, Rectangle):
            return self.get_area() <= other.get_area()
        raise ValueError("Unsupported operand type for <=")

    def __gt__(self, other):
        if isinstance(other, Rectangle):
            return self.get_area() > other.get_area()
        raise ValueError("Unsupported operand type for >")

    def __ge__(self, other):
        if isinstance(other, Rectangle):
            return self.get_area() >= other.get_area()
        raise ValueError("Unsupported operand type for >=")

    def __str__(self):
        """
        Возвращает строковое представление прямоугольника.

        Returns:
            str: Строковое представление.
        """
        return f'Rectangle: height = {self.height}, width = {self.width}'

spam = Rectangle(1, 9)
eggs = Rectangle(7)

add_reg = spam + eggs
sub_reg = spam - eggs

print(add_reg)
print(sub_reg)

print(f"spam равен eggs: {spam == eggs}")
print(f"spam не равен eggs: {spam != eggs}")
print(f"spam меньше eggs: {spam < eggs}")
print(f"spam меньше или равен eggs: {spam <= eggs}")
print(f"spam больше eggs: {spam > eggs}")
print(f"spam больше или равен eggs: {spam >= eggs}")

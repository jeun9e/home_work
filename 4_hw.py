# Задача 1. Площадь и периметр прямоугольника
class rectangle:
    def __init__(self, wid, lenght):
        self.wid = wid
        self.lenght = lenght

    def square(self):
        return self.wid * self.lenght

    def perimeter(self):
        return self.wid*2+self.lenght*2


Area = rectangle(4, 10)
Perim = rectangle (3, 10)

print(Area.square())
print(Perim.perimeter())





# Задача 2.

class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b


    def addition(self):
        return  self.a + self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b

    def subtraction(self):
        return self.a - self.b

action = Math(100, 20)

print(action.addition(), action.multiplication(), action.division(), action.subtraction())

# Задача 3 demoqa

class Elements:
    def __init__(self, text, type, loc):
        self.text = text
        self.type = type
        self.loc = loc

    def click(self):
        print('Клик по кнопке: ' + self.text)


one = Elements ('TextBox', 'Кнопка', ' ')
two = Elements ('Check Box', 'Кнопка', '')
three = Elements ('Radio Button', 'Кнопка', '')
four = Elements ('Web Tables', 'Кнопка', '')
five = Elements ('Buttons', 'Кнопка', '')
six = Elements ('Links', 'Кнопка', '')
seven = Elements ('Broken Links - Images', 'Кнопка', '')
eight = Elements ('Upload and Dowload', 'Кнопка', '')
nine = Elements ('Dynamic Properties', 'Кнопка', '')

print(one.type, one.text + '\n', two.type, two.text + '\n', three.type, three.text)
nine.click()
one.click()

#Задача 4. Машина
class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start(self):
        print('Автомобиль заведен')

    def stop(self):
        print('Автомобиль заглушен')

    def display(self):
        # print(f"Марка:{self.color}, Model: {self.type}, Year: {self.year}")
        print('Цвет:' + self.color, 'Модель:' + self.type, 'Год выпуска:' + self.year)
a = Car ('Blue', 'BMW', '2022')
a.display()

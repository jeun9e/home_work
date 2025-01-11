# Задача 1
def task_1() -> str:
  a: int = 10
  b: float = 10.5
  c: str = 'Задача 1'
  d: list = [5, 10, 15, 20]
  e: bool = True
  return type(a), type(b), type(c), type (d), type (e)
print (task_1())


# Задача 2
def task_2() -> list:
  a: list = [1, 2, 3, 5, 8, 13, 21]
  return a[0:3]
print(task_2())
# Числа Фибоначчи


# Задача 3
def task_3(a: int) -> int:
  return a*a
print(task_3(11))

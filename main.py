# Створіть клас для представлення користувача з
# атрибутами: ім'я та вік. Додайте властивості для
# валідації віку користувача. Наприклад, вік повинен
# бути у межах від 0 до 120.

class User:
    def __init__(self, name, age, max_age):
        self._name = name
        self._age = age
        self._max_age = max_age
    @property
    def name(self):
        return self._name
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        if value <= self._max_age:
            self._age = value
        else:
            raise ValueError("Value is too high")



user = User("John", 40, 120)
user.age = 40
print(user.name, user.age)
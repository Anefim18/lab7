# Дженеричний клас репозиторію
class Repository<T>:

    # Список елементів, що зберігаються в репозиторії

    _elements = []

    # Додати елемент у репозиторій

    def add(self, element):
        self._elements.append(element)

    # Видалити елемент із репозиторію

    def remove(self, element):
        self._elements.remove(element)

    # Отримати список усіх елементів

    def get_all(self):
        return self._elements

    # Знайти всі елементи, що задовольняють критерію

    def find(self, criteria):
        return [element for element in self._elements if criteria(element)]


# Приклад використання репозиторію з критеріями

def main():
    # Репозиторій для цілих чисел
    int_repository = Repository<int>()
    int_repository.add(1)
    int_repository.add(2)
    int_repository.add(3)

    # Критерій, який повертає True для парних чисел
    def is_even(x):
        return x % 2 == 0

    # Знаходимо всі парні числа
    even_numbers = int_repository.find(is_even)
    print(even_numbers)

    # Репозиторій для строк
    string_repository = Repository<str>()
    string_repository.add("Hello")
    string_repository.add("World")
    string_repository.add("Python")

    # Критерій, який повертає True для строк, що починаються з букви "H"
    def starts_with_h(x):
        return x[0] == "H"

    # Знаходимо всі строки, що починаються з букви "H"
    h_strings = string_repository.find(starts_with_h)
    print(h_strings)


if __name__ == "__main__":
    main()

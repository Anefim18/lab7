# Дженеричний клас калькулятора
class Calculator<T>:

    # Делегати для основних арифметичних операцій

    add_delegate = Delegate<T, T, T>()
    subtract_delegate = Delegate<T, T, T>()
    multiply_delegate = Delegate<T, T, T>()
    divide_delegate = Delegate<T, T, T>()

    # Методи, які використовують делегати для виконання відповідних арифметичних операцій

    def add(self, x, y):
        return self.add_delegate(x, y)

    def subtract(self, x, y):
        return self.subtract_delegate(x, y)

    def multiply(self, x, y):
        return self.multiply_delegate(x, y)

    def divide(self, x, y):
        return self.divide_delegate(x, y)


# Приклад використання калькулятора для різних типів даних

def main():
    # Калкулятор для цілих чисел
    int_calculator = Calculator<int>()
    int_calculator.add_delegate = lambda x, y: x + y
    int_calculator.subtract_delegate = lambda x, y: x - y
    int_calculator.multiply_delegate = lambda x, y: x * y
    int_calculator.divide_delegate = lambda x, y: x / y

    print(int_calculator.add(1, 2))
    print(int_calculator.subtract(3, 2))
    print(int_calculator.multiply(2, 3))
    print(int_calculator.divide(6, 2))

    # Калкулятор для двійкових чисел
    float_calculator = Calculator<float>()
    float_calculator.add_delegate = lambda x, y: x + y
    float_calculator.subtract_delegate = lambda x, y: x - y
    float_calculator.multiply_delegate = lambda x, y: x * y
    float_calculator.divide_delegate = lambda x, y: x / y

    print(float_calculator.add(1.1, 2.2))
    print(float_calculator.subtract(3.3, 2.2))
    print(float_calculator.multiply(2.2, 3.3))
    print(float_calculator.divide(6.6, 2.2))


if __name__ == "__main__":
    main()

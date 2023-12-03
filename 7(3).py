# Дженеричний клас кешу
class FunctionCache<TKey, TResult>:

    # Список ключів, що зберігаються в кеші

    _keys = []

    # Список результатів, що зберігаються в кеші

    _results = []

    # Час дії кешованих результатів

    _expiration_time = None

    # Створити новий кеш

    def __init__(self, expiration_time=None):
        self._expiration_time = expiration_time

    # Додати функцію до кешу

    def add(self, key, function):
        self._keys.append(key)
        self._results.append(None)

    # Отримати результат виконання функції з кешу

    def get(self, key):
        # Якщо ключ не знайдено, поверніть None
        if key not in self._keys:
            return None

        # Якщо результат не прострочений, поверніть його
        result = self._results[self._keys.index(key)]
        if result is not None and (self._expiration_time is None or time.time() <= result.expiration_time):
            return result.result

        # В іншому випадку виконайте функцію і додайте результат у кеш
        result = function(key)
        self._results[self._keys.index(key)] = Result(result, time.time() + self._expiration_time)
        return result


# Клас результату виконання функції
class Result:

    def __init__(self, result, expiration_time):
        self.result = result
        self.expiration_time = expiration_time


# Приклад використання кешу

def main():
    # Кеш з терміном дії 1 секунда
    cache = FunctionCache(1)

    # Додаємо функцію до кешу
    cache.add("key1", lambda x: x * 2)

    # Отримуємо результат виконання функції з кешу
    result = cache.get("key1")
    print(result)

    # Отримуємо результат виконання функції з кешу ще раз
    # (результат буде той самий, оскільки він ще не прострочений)
    result = cache.get("key1")
    print(result)

    # Час дії результату минув
    time.sleep(1.1)

    # Отримуємо результат виконання функції з кешу ще раз
    # (результат буде новим, оскільки попередній прострочений)
    result = cache.get("key1")
    print(result)


if __name__ == "__main__":
    main()

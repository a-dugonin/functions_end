from collections import Counter


def can_be_poly(string: str):
    """Функция проверяет, является ли переданная на вход строка палиндромом"""
    if isinstance(string, str):
        return len(string) % 2 == sum(value % 2 for value in Counter(string).values())
    return "В функцию передан не строковый аргумент"

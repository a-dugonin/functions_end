from collections import Counter

message = "Today is a beautiful day! The sun is shining and the birds are singing."


def count_unique_characters(message: str) -> int or str:
    """ Функция подсчитывает количество уникальных символов в переданной строке """
    if isinstance(message, str):
        return sum(map(lambda count: count == 1, Counter(message).values()))
    else:
        raise ValueError("Error: В функцию передан аргумент не являющийся строковым")

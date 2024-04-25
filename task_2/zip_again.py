from typing import List, Tuple

letters: List[str] = ['a', 'b', 'c', 'd', 'e']
numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]

result_zip: List[Tuple[int or str]] = list(zip(letters, numbers))

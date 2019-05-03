from collections import Iterator


def fun(text: str) -> Iterator[int]:
    return map(len, text.split())


def nothing(x: int) -> None:
    pass



nothing(1.23342)
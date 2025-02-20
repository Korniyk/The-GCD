import math
import pytest


def gcd(a: int, b: int) -> int:
    """Функція для знаходження найбільшого спільного дільника двох чисел."""
    return math.gcd(a, b)


def main():
    print("Додаток для знаходження найбільшого спільного дільника")
    try:
        a = int(input("Введіть перше число: "))
        b = int(input("Введіть друге число: "))
        print(f"НСД({a}, {b}) = {gcd(a, b)}")
    except ValueError:
        print("Будь ласка, введіть коректні цілі числа.")


if __name__ == "__main__":
    main()


def test_gcd():
    assert gcd(48, 18) == 6
    assert gcd(101, 10) == 1
    assert gcd(56, 98) == 14
    assert gcd(0, 5) == 5
    assert gcd(7, 0) == 7

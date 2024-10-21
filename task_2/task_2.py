import re
from typing import Callable


def generator_numbers(text: str):
    pattern = re.compile(r' \d+.\d+ ')
    nums = pattern.findall(text)
    for num in nums:
        yield float(num.strip())


def sum_profit(text: str, func: Callable):
    sum = 0
    generator = func(text)
    try:
        while True:    
            sum += next(generator)
    except StopIteration:
        return sum


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}") # Result must be 1351.46

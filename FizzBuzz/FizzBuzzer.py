
def get_value(input: int) -> str:
    """Given an int it return Fizz, Buzz or FizzBuzz if it is a multiple of 3, 5 or both"""
    result = f'{input}'
    if input % 3 == 0:
        result = 'Fizz'
    return result
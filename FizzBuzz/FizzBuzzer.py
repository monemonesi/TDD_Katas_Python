
def get_value(input: int) -> str:
    """Given an int it return Fizz, Buzz or FizzBuzz if it is a multiple of 3, 5 or both"""
    if input % 3 == 0:
        return 'Fizz'
    elif input % 5 == 0:
        return 'Buzz'
    else:
        return f'{input}'
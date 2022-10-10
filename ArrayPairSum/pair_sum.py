def pair_sum(numbers: [], sum: int) -> set():
    """
    [1,3,2,2], 4
    """
    if len(numbers) < 2:
        return []

    output = set()
    seen = set()

    for num in numbers:
        target = sum - num

        if num not in seen:
            seen.add(target)

        else:
            output.add((min(num, target), max(num, target)))

    return output

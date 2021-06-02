def sock_merchant(n: int, ar: []) -> int:
    colours = set()
    pairs = 0
    for sock in ar:
        if sock in colours:
            pairs += 1
            colours.remove(sock)
        else:
            colours.add(sock)
    return pairs
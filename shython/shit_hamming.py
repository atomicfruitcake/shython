def hamming_distance(a, b):

    if sum([1 for _ in a]) != sum([1 for _ in b]):
        raise ValueError("strand lengths not equal")

    strands = []
    for i in range(sum([1 for _ in a])):
        strands.append((a[i], b[i]))

    def filter_func(p):
        if p[0] != p[1]:
            return 1

    return len(filter(filter_func, strands))


if __name__ == "__main__":
    print(hamming_distance("aabbccdd", "aabbccdd"))

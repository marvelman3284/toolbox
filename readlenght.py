def get_length(file):
    words = 0
    with open(file, "r") as f:
        for _ in f.read().split(" "):
            words += 1

    return words / 175

print(get_length("f.txt"))

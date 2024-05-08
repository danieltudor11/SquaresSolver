


def get_words_list():
    words = []
    with open('words_alpha.txt') as file:
        for line in file:
            line = line.strip()
            if len(line) > 3 and len(line) < 17:
                words.append(line)
    return words


def print_results(res):
    res = dict(sorted(res.items()))
    for k,v in res.items():
        print(f"The {k}-letter words are: {v}")
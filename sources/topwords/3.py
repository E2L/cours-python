def clean_fragment(fragment):
    result = ""
    for c in fragment:
        if c.isalpha() or c in ["-", "'"]:
            result += c

    return result


def split_words(text):
    fragments = split_fragments(text)
    res = list()
    for fragment in fragments:
        fragment = fragment.lower()
        fragment = clean_fragment(fragment)
        if fragment:
            res.append(fragment)
    return res


def split_fragments(text):
    res = list()
    for fragment in text.split():
        if "’" in fragment:
            (before, after) = fragment.split("’")
            res.append(before)
            res.append(after)
        else:
            res.append(fragment)
    return res


def get_frequencies(words):
    res = dict()
    for word in words:
        if word in res:
            res[word] += 1
        else:
            res[word] = 1
    return res


words = ["pomme", "poire", "banane", "poire", "banane", "banane"]
frequencies = get_frequencies(words)
print(frequencies)

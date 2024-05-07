list_1 = [1, 2, 3, 4, 5]
k = 6
closest_el = min(list_1, key=lambda x: abs(x - k))
print(closest_el)


list_1 = [1, 2, 3, 4, 5]
k = 3
count_k = list_1.count(k)
print(count_k)


k = 'ноутбук'
english_scores = {
    "A": 1,
    "E": 1,
    "I": 1,
    "O": 1,
    "U": 1,
    "L": 1,
    "N": 1,
    "S": 1,
    "T": 1,
    "R": 1,
    "D": 2,
    "G": 2,
    "B": 3,
    "C": 3,
    "M": 3,
    "P": 3,
    "F": 4,
    "H": 4,
    "V": 4,
    "W": 4,
    "Y": 4,
    "K": 5,
    "J": 8,
    "X": 8,
    "Q": 10,
    "Z": 10,
}
russian_scores = {
    "А": 1,
    "В": 1,
    "Е": 1,
    "И": 1,
    "Н": 1,
    "О": 1,
    "Р": 1,
    "С": 1,
    "Т": 1,
    "Д": 2,
    "К": 2,
    "Л": 2,
    "М": 2,
    "П": 2,
    "У": 2,
    "Б": 3,
    "Г": 3,
    "Ё": 3,
    "Ь": 3,
    "Я": 3,
    "Й": 4,
    "Ы": 4,
    "Ж": 5,
    "З": 5,
    "Х": 5,
    "Ц": 5,
    "Ч": 5,
    "Ш": 8,
    "Э": 8,
    "Ю": 8,
    "Ф": 10,
    "Щ": 10,
    "Ъ": 10,
}

def calc_score(word, scores):
    score = 0
    for letter in word:
        score += scores[letter.upper()]
    return score

alphabet_language = None

if k[0].upper() in english_scores:
    alphabet_language = "english"
elif k[0].upper() in russian_scores:
    alphabet_language = "russian"

if alphabet_language == "english":
    score = calc_score(k, english_scores)
elif alphabet_language == "russian":
    score = calc_score(k, russian_scores)

print("Стоимость слова '{}': {}".format(k, score))

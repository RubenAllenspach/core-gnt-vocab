import csv
# import pprint


def get_lines(file):
    words = []

    with open(file, encoding='utf8') as top50list:
        for line in top50list:
            parts = line.strip().split(' ')

            words.append((parts[0], parts[1], parts[2], ' '.join(parts[3:])))

    return words


def get_lines_lemma(file):
    words = []

    with open(file, encoding='utf8') as top50list:
        for line in top50list:
            parts = line.strip().split(' ')

            words.append((parts[0], parts[1], ' '.join(parts[2:])))

    return words


file_names = [
    'form_50',
    'form_80',
    'form_90'
]

for file_name in file_names:
    with open(file_name + '.csv', mode='w', encoding='utf8', newline='') as form_50:
        form_50_writer = csv.writer(form_50, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for word_row in get_lines(file_name + '.txt'):
            form_50_writer.writerow([word_row[0], word_row[3]])


file_names_lemma = [
    'lemma_50',
    'lemma_80',
    'lemma_90',
    'lemma_95'
]

for file_name in file_names_lemma:
    with open(file_name + '.csv', mode='w', encoding='utf8', newline='') as form_50:
        form_50_writer = csv.writer(form_50, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for word_row in get_lines_lemma(file_name + '.txt'):
            form_50_writer.writerow([word_row[0], word_row[2]])

# pp = pprint.PrettyPrinter(indent=4, depth=2)
# pp.pprint(words)

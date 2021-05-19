import os
import json


def clean_text(raw_text):
    substr_to_remove = ['[', '\n', ']', '\t', '\r']
    cur_string = str(raw_text)
    for substr in substr_to_remove:
        cur_string = cur_string.replace(substr, '')
    return cur_string


def read_in_files(dir='data', select_files=[]):

    files = os.listdir(dir)
    full_raw_text = ""
    if select_files == []:
        select_files = files

    for file in files:
        if file in select_files:
            with open(os.path.join(dir, file), 'rb') as text_file:
                text = text_file.read()
                full_raw_text += text.decode("ISO-8859-1")

    return clean_text(full_raw_text)


def add_next_ngram(table, remaining_text, n):

    ngram = remaining_text[:n]
    next_char = remaining_text[n]
    if ngram in table:
        next_char_table = table[ngram]

        if next_char in next_char_table:
            next_char_table[next_char] += 1
        else:
            next_char_table[next_char] = 1

    else:
        table[ngram] = {next_char: 1}

    return table


def form_ngrams(text, n):

    table = {}
    # start = text[:n]
    # table[start] = [text[n]]

    remaining_text = text

    while len(remaining_text) > n:
        table = add_next_ngram(table, remaining_text, n)
        remaining_text = remaining_text[1:]

    return table


def write_out_to_json(n):
    text = read_in_files()
    table = form_ngrams(text, n)

    with open('ngrams.json', 'w') as fp:
        json.dump(table, fp)


if __name__ == "__main__":
    write_out_to_json(9)
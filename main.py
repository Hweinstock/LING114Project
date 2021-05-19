import json
import random
from n_gram import form_ngrams, read_in_files


def load_in_json(path='ngrams.json'):
    with open(path) as file:
        data = json.load(file)
    return data


def select_next_char(options):

    distribution_list = []
    for next_char in options:
        temp_list = [next_char for i in range(options[next_char])]
        distribution_list += temp_list
    return random.choice(distribution_list)


def real_length(my_string):
    return len([char for char in my_string if char.isalpha()])


def generate_text(table, prompt, length):
    if prompt not in table:
        print("Unable to find prompt!")
        return "-1"
    else:
        result_str = prompt
        next_kgram = prompt
        while real_length(result_str) < length:
            options = table[next_kgram]
            next_char = select_next_char(options)
            next_kgram = next_kgram[1:] + next_char
            result_str += next_char

    return result_str


def generate_text_from_files(files, n, k):

    text = read_in_files(select_files=files)
    table = form_ngrams(text, k)
    prompt = random.choice(list(table.keys()))
    generated_txt = generate_text(table, prompt, n)
    return generated_txt


if __name__ == "__main__":

    # Generate the Text

    text_A_filter = ["shakespeare-caesar.txt", "shakespeare-hamlet.txt", "shakespeare-macbeth.txt"]
    text_A_1 = generate_text_from_files(files=text_A_filter, n=1000, k=1)
    text_A_2 = generate_text_from_files(files=text_A_filter, n=1000, k=5)
    text_A_3 = generate_text_from_files(files=text_A_filter, n=1000, k=9)
    print("Done generating A...")
    print("Text A")
    print("k=1")
    print(text_A_1)
    print("k=5")
    print(text_A_2)
    print("k=9")
    print(text_A_3)

    text_B_filter = ["melville-moby_dick.txt"]
    text_B_1 = generate_text_from_files(files=text_B_filter, n=1000, k=1)
    text_B_2 = generate_text_from_files(files=text_B_filter, n=1000, k=5)
    text_B_3 = generate_text_from_files(files=text_B_filter, n=1000, k=9)
    print("Done generating B...")

    print("Text B")
    print("k=1")
    print(text_B_1)
    print("k=5")
    print(text_B_2)
    print("k=9")
    print(text_B_3)

    text_C_filter = ["austen-emma.txt", "blake-poems.txt", "edgeworth-parents.txt", "milton-paradise.txt"]
    text_C_1 = generate_text_from_files(files=text_C_filter, n=500, k=1)
    text_C_2 = generate_text_from_files(files=text_C_filter, n=500, k=5)
    text_C_3 = generate_text_from_files(files=text_C_filter, n=500, k=9)
    print("Done generating C...")

    print("Text C")
    print("k=1")
    print(text_C_1)
    print("k=5")
    print(text_C_2)
    print("k=9")
    print(text_C_3)



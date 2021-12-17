def get_word_from_text(filename):
    with open(filename, 'wr', encoding='utf-8') as file:
        return file.read().splitlines()

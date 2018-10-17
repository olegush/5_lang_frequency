import os.path
import sys
import string
import collections


def load_data(filepath):
    with open(filepath, 'rb') as file:
        return file.read()


def get_most_frequent_words(text):
    words_quantity = 10
    formatted_text = text.translate(None, '\n\r\r{}'
                                    .format(string.punctuation)).lower()
    formatted_text_list = formatted_text.split(' ')
    return collections.Counter(
        filter(lambda item: item != '',
               formatted_text_list)).most_common(words_quantity)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        exit('need parameter')
    user_filepath = sys.argv[1]
    if not os.path.exists(user_filepath):
        exit('need correct file path')
    user_text = load_data(user_filepath)
    print('The 10 most_frequent_words in the text:')
    for word in get_most_frequent_words(user_text):
        print('"{}"'.format(word[0]))

import sys
import string
import collections


def load_data(filepath):
    with open(filepath, 'r') as file:
        return file.read()


def get_most_frequent_words(data_txt):
    words_quantity = 10
    # не понимаю что ломается. все языки перепробовал. поясните
    formatted_text = data_txt.translate(
        None, '\n\r\r{}'.format(string.punctuation)
    ).lower()
    most_frequent_words_list = collections.Counter(
        filter(lambda item: item != '', formatted_text.split(' '))
    ).most_common(words_quantity)
    return most_frequent_words_list


if __name__ == '__main__':
    try:
        user_filepath = sys.argv[1]
        user_data_txt = load_data(user_filepath)
    except IndexError:
        print('No script parameter (path to txt file)')
    except IOError:
        print('No such file or directory')
    else:
        print('The 10 most_frequent_words in the text:')
        for word, quantity in get_most_frequent_words(user_data_txt):
            print('"{}"'.format(word))

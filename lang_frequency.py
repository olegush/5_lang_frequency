import sys
import string
import collections


def load_data(filepath):
    with open(filepath, 'r') as file:
        return file.read()


def get_most_frequent_words(data_txt):
    words_quantity = 10
    trans_dict = dict.fromkeys(string.punctuation)
    trans_dict.update({'\n': None, '\r': None, '\t': None})
    translator = str.maketrans(trans_dict)
    data_txt = data_txt.translate(translator).lower()
    most_frequent_words_list = collections.Counter(
        filter(lambda item: item != '', data_txt.split(' '))
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

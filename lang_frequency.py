import sys
import string
import collections


def load_data(filepath):
    with open(filepath, 'r') as file:
        return file.read()


def get_most_frequent_words(data_txt):
    words_quantity = 10
    formatted_text = data_txt.translate(
        None, '\n\r\r{}'.format(string.punctuation)
    ).lower()
    most_frequent_words_list = collections.Counter(
        filter(lambda item: item != '', formatted_text.split(' '))
    ).most_common(words_quantity)
    most_frequent_words = ''
    for word, quantity in most_frequent_words_list:
        most_frequent_words += '"{}"\n'.format(word)
    return most_frequent_words


if __name__ == '__main__':
    try:
        user_filepath = sys.argv[1]
        user_data_txt = load_data(user_filepath)
        print('The 10 most_frequent_words in the text:')
        print(get_most_frequent_words(user_data_txt))
    except IndexError:
        print('No script parameter (path to txt file)')
    except IOError:
        print ('No such file or directory')
    except ValueError:
        print('No text in the file)')

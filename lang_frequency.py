import sys
import string
import collections


def load_data(filepath):
    with open(filepath, 'r') as file:
        return file.read()


def get_most_frequent_words(data):
    words_quantity = 10
    formatted_text = data.translate(
        None, '\n\r\r{}'.format(string.punctuation)
    ).lower()
    formatted_list = filter(lambda item: item != '', formatted_text.split(' '))
    return collections.Counter(formatted_list).most_common(words_quantity)


if __name__ == '__main__':
    try:
        user_filepath = sys.argv[1]
        user_data = load_data(user_filepath)
        print('The 10 most_frequent_words in the text:')
        for word, quantity in get_most_frequent_words(user_data):
            print('"{}"'.format(word))
    except IndexError:
        print('No script parameter (path to txt file)')
    except IOError:
        print ('No such file or directory')
    except ValueError:
        print('No text in the file)')

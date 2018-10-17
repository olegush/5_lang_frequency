import os.path
import sys
import string


def load_data(filepath):
    with open(filepath, 'rb') as file:
        return file.read()


def get_most_frequent_words(text):
    formatted_text = text.translate(None, '\n\r\r{}'
                                    .format(string.punctuation)).lower()
    formatted_text_list = formatted_text.split(' ')
    most_frequent_words_dict = {}
    for word in formatted_text_list:
        most_frequent_words_dict[word] = formatted_text_list.count(word)
    return sorted(most_frequent_words_dict,
                  key=most_frequent_words_dict.get, reverse=True)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        exit('need parameter')
    user_filepath = sys.argv[1]
    if not os.path.exists(user_filepath):
        exit('need correct file path')
    user_text = load_data(user_filepath)
    ten_most_frequent_words = get_most_frequent_words(user_text)[0:10]
    ten_most_frequent_words.remove('')
    print('The 10 most_frequent_words in the text:')
    for word in ten_most_frequent_words:
        print('"{}"'.format(word))

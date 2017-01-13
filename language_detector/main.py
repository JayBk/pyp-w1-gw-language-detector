# -*- coding: utf-8 -*-
from languages import LANGUAGES

def detect_language(text, languages):
    """Returns the detected language of given text."""
    clean_list = text.split()
    
    max_counter = 0
    most = ""
    for lang in languages:
        common = [x for x in clean_list if x in lang['common_words']]
        if len(common) > max_counter:
            most = lang['name']
            max_counter = len(common)
    return most
    
if __name__=='__main__':
    text = input('Enter the text you want to know the language for:')
    the_language = detect_language(text, LANGUAGES)
    print('The language of the text: \n \
    \" {}.\" \n Is {}.'.format(text, the_language))
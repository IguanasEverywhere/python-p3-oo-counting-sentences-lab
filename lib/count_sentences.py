#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        self.value = value

    def get_value(self):
        return self._value

    def set_value(self, value):
        if (type(value) == str):
            self._value = value
        else:
            print('The value must be a string.')

    value = property(get_value, set_value)

    def is_sentence(self):
        return self._value.endswith('.')

    def is_question(self):
        return self._value.endswith('?')

    def is_exclamation(self):
        return self._value.endswith('!')

    def count_sentences(phrase):

        phrase_without_exclams = phrase.value.replace('!', '.')
        phrase_with_periods_only = phrase_without_exclams.replace('?', '.')
        phrase_as_list = phrase_with_periods_only.split('.')
        list_without_empties = []
        for word in phrase_as_list:
            if (word != ''):
                list_without_empties.append(word)
        return len(list_without_empties)




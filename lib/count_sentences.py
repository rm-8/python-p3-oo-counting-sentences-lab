#!/usr/bin/env python3

import re

class MyString:
    def __init__(self, value=''):
        if isinstance(value, str):
            self.value = value
        else:
            raise ValueError("Value must be a string.")

    def is_sentence(self):
        if self.value.endswith('.'):
            return True
        else:
            return False

    def is_question(self):
        if self.value.endswith('?'):
            return True
        else:
            return False

    def is_exclamation(self):
        if self.value.endswith('!'):
            return True
        else:
            return False

    def count_sentences(self):
        # Split the string based on '.', '!', and '?' and remove empty strings
        sentences = [sentence for sentence in re.split(r'[.!?]', self.value) if sentence.strip()]
        return len(sentences)

    
  
import random
import pickle
import os
import string

class LexBuilder():

    def __init__(self):
        self.path = 'dictionary.p'
        if os.path.exists(self.path):
            self.known_words = pickle.load(open(self.path, 'rb'))
        else:
            self.known_words = {}
            self.known_words = {"":"", "negation": "no", "all": "ko", "present_progressive": "ma", "speak":"lun", "nominal": "do", "verbal": "va", "object": "pe", "reflexive": "sido"}

    def translate(self, word):
        if word in self.known_words:
            return self.known_words[word]
        else:
            return self.add_new_word(word)

    def transliterate(self, words):
        final_word = ""
        for word in words.split():
            final_word += self.translate(word)
        return final_word

    def add_new_word(self, word):
        transliteration = input(word + " not found. Input an empty string to generate, input ! to assign, or input transliteration: ")
        if transliteration == "":
            new_word = self.make_random()
        elif transliteration == "!":
            new_word = input("What should " + word + " be saved as? ")
        else:
            new_word = self.transliterate(transliteration)
        print("adding", word, "as", new_word)
        self.known_words[word] = new_word
        self.save()
        return new_word
        
    def make_random(self):
        word = ""
        consonants = ['d', 'k', 'g', 't', 's', 'z', 'b', 'p', 'S', 'C', 'l', 'J', 'T', 'v']
        vowels = ['a', 'i', 'u', 'e', 'o']
        nasals = ['m', 'n']

        while word in self.known_words:
            word = ""
            word += random.choice(consonants)
            word += random.choice(vowels)
            if random.choice([True, False]):
                word += random.choice(consonants)
                word += random.choice(vowels)
            if random.choice([True, False]):
               word += random.choice(nasals) 
        return word
    
    @staticmethod
    def clean_and_split(s):
        exclude = set(string.punctuation)
        s = ''.join(ch for ch in s if ch not in exclude)
        s = s.lower()
        s = s.split()
        return s

    def save(self):
        pickle.dump(self.known_words, open(self.path, 'wb'))

    def translate_list_of_words(self, x):
        words = self.clean_and_split(x)
        for word in words:
            self.translate(word)

    def dump_dictionary(self):
        for word in self.known_words:
            print(word, ":", self.known_words[word])

lex = LexBuilder()
lex.translate_list_of_words(input("put in a string of many words to translate: "))
lex.dump_dictionary()

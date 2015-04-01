__author__ = 'ariyatan'
import csv

#list of adjectives that have synthetic forms of degree of comparison
synth_form_list = []
with open('adj_comp_ex.csv', 'rb') as dc:
    for line in dc:
        synth_form_list.append(line[:-1])
        #I use [:-1] to get rid of '\n' symbol at the end of each row

#list of adjectives that double last consonant in synthetic form
double_cons_list = []
with open('adj_double_consonant.csv', 'rb') as lst:
    for line in lst:
        double_cons_list.append(line[:-1])
        #I use [:-1] to get rid of '\n' symbol at the end of each row

#stem ending in 'y' don't change if it's part of a diphtong and follows a vowel
no_change_list = ['shy', 'gray', 'sly', 'spry', 'wry']

#Synthetic forms are by adjectives with 1-syllable stem, or with 2-syllable stem, if it ends in 'er' (like 'clever'), 'y' (like 'dirty'), 'le' (like 'simple') or 'ow' (like 'narrow')
#Adjectives of 2 and more syllables usually have analytic forms of comparison

class adj_form(object):
    def __init__(self, stem, degree = '0'):
        self.stem = stem
        self.degree = degree

    def add_er(self):
        if self.stem[-1] == 'y':
            if self.stem in no_change_list:
                return self.stem + 'er'
            else:
                return self.stem[:-1] + 'ier'
        if self.stem[-1] == 'e':
            return self.stem + 'r'
        if self.stem in double_cons_list:
            return self.stem + self.stem[-1] + 'er'
        else:
            return self.stem + 'er'

    def add_est(self):
        if self.stem[-1] == 'y':
            if self.stem in no_change_list:
                return self.stem + 'er'
            else:
                return self.stem[:-1] + 'iest'
        if self.stem[-1] == 'e':
            return self.stem + 'st'
        if self.stem in double_cons_list:
            return self.stem + self.stem[-1] + 'est'
        else:
            return self.stem + 'est'


    def comparative(self):
        if self.stem == 'good':
            return 'better'
        if self.stem == 'bad':
            return 'worse'
        if self.stem == 'little':
            return 'lesser'
        if self.stem in synth_form_list:
            return self.add_er()
        else:
            return 'more' + ' ' + self.stem

    def superlative(self):
        if self.stem == 'good':
            return 'best'
        if self.stem == 'bad':
            return 'worst'
        if self.stem == 'little':
            return 'least'
        if self.stem in synth_form_list:
            return self.add_est()
        else:
            return 'the most' + ' ' + self.stem

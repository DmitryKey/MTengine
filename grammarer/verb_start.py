__author__ = 'ariyatan'
from verb_tenses import verb_form

def verb_input():
    v_input = raw_input('Enter a verb> \n')
    return v_input


def tense_input():
    tense = raw_input('Enter the required tense > \n')
    return tense


def person_input():
    person = raw_input('Enter the person > \n')
    return person


def tense_choice(tense, case):
    if tense in ['present simple', 'ps']:
        return verb_form.present_simple(case)
    elif tense in ['gerund', 'g']:
        return verb_form.gerund(case)
    elif tense in ['participle', 'ppl']:
        return verb_form.ppl(case)
    elif tense in ['present perfect', 'prp']:
        return verb_form.present_perfect(case)
    elif tense in ['past simple', 'pas']:
        return verb_form.past_simple(case)
    elif tense in ['future simple', 'fs']:
        return verb_form.future_simple(case)
    elif tense in ['present continuous', 'pc']:
        return verb_form.present_continuous(case)
    elif tense in ['past perfect', 'pap']:
        return verb_form.past_perfect(case)
    elif tense in ['future continuous', 'fc']:
        return verb_form.future_continuous(case)
    elif tense in ['past continuous', 'pac']:
        return verb_form.past_continuous(case)
    else:
        return verb_form.inf(case)


print '''Welcome to the test interface for verb form generator!
The interface will ask you to provide verb, and fill tense and person, to which it would bend.
It's very simple and has no spell check, so be careful not to make mistakes.

'verb' is an open category, so you can print any verb you like.
'tense' can be present simple, present perfect, present continuous, past continuous, future continuous, past simple, past perfect, and also gerund and participle.
'person' can be can be 'I','you','she' (we try to be correct), 'we' or 'they'.

You need to fill in at least verb and tense for the first time.
If later some input is empty, the interface will use your previous choices. \nThe idea is to give you possibility to test different forms for the same verb or the same person without extra typing

You can use acronyms for a faster input of tenses:
g - gerund
ppl - participle
ps - present simple
prp - present perfect
pap - past perfect
pas - past simple
fs - future simple
pc - present continuous
fc - future continuous
pac - past continuous

'''
#main

verb = verb_input()
tense = tense_input()
person = person_input()

case = verb_form(verb, tense, person)

print tense_choice(tense, case)

while True:
    v = verb_input()
    if v != '':
        verb = v

    t = tense_input()
    if t != '':
        tense = t

    p = person_input()
    if p != '':
        person = p

    if tense == '':
        tense = 'inf'
    else:
        pass

    case = verb_form(verb, tense, person)

    print tense_choice(tense, case)

    print "\nLet's test some more"



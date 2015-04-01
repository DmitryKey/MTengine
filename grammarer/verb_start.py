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
    if tense == 'present simple':
        return verb_form.present_simple(case)
    elif tense == 'gerund':
        return verb_form.gerund(case)
    elif tense == 'pp2':
        return verb_form.pp2(case)
    elif tense == 'present perfect':
        return verb_form.present_perfect(case)
    elif tense == 'past simple':
        return verb_form.past_simple(case)
    elif tense == 'future simple':
        return verb_form.future_simple(case)
    elif tense == 'present continuous':
        return verb_form.present_continuous(case)
    elif tense == 'past perfect':
        return verb_form.past_perfect(case)
    elif tense == 'future continuous':
        return verb_form.future_continuous(case)
    elif tense == 'past continuous':
        return verb_form.past_continuous(case)
    else:
        return verb_form.inf(case)


print '''Welcome to the test interface for verb form generator!
The interface will ask you to provide verb, and fill tense and person, to which it would bend.
It's very simple and has no spell check, so be careful not to make mistakes.

'verb' is an open category, so you can print any verb you like.
'tense' can be present simple, present perfect, present continuous, past continuous, future continuous, past simple, past perfect, and also gerund and pp2 (participle 2)
'person' can be can be 'I','you','she' (we try to be correct), 'we' or 'they'.

You need to fill in at least verb and tense for the first time.
If later some input is empty, the interface will use your previous choices. \nThe idea is to give you possibility to test different forms for the same verb or the same person without extra typing

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



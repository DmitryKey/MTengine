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
    elif tense == 'pp1':
        return verb_form.pp1(case)
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
    else:
        return verb_form.inf(case)


def start(verb, tense, person):

    if tense == '':
        tense = 'inf'
    else:
        pass
    case = verb_form(verb, tense, person)

    print tense_choice(tense, case)

    print "\nLet's test some more"

    restart (verb, tense, person)


def restart(verb, tense, person):
    v = verb_input()
    if v == '':
        pass
    else:
        verb = v

    t = tense_input()
    if t == '':
        pass
    else:
        tense = t

    p = person_input()
    if p == '':
        pass
    else:
        person = p

    if tense == '':
        tense = 'inf'
    else:
        pass

    case = verb_form(verb, tense, person)


    print tense_choice(tense, case)

    print "\nLet's test some more"

    restart (verb, tense, person)

print '''Welcome to the test interface for verb form generator!
The interface will ask you to provide verb, and fill tense and person, to which it would bend.
It's very simple and has no spell check, so be careful not to make mistakes.

'verb' is an open category, so you can print any verb you like.
'tense' can be present simple, present perfect, present continuous, past simple, past perfect, and also pp1 (participle 1) and pp2 (participle 2)
'person' can be can be 'I','you','she' (we try to be correct), 'we' or 'they'.

You need to fill in at least verb and tense for the first time.
If later some input is empty, the interface will use your previous choices. \nThe idea is to give you possibility to test different forms for the same verb or the same person without extra typing

'''


verb = verb_input()
tense = tense_input()
person = person_input()

start(verb, tense, person)


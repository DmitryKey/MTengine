import csv

reader = csv.reader(open('noun_exceptions.csv'))
noun_exceptions = {}

for row in reader:
    key = row[0]
    noun_exceptions[key] = row[1]

no_plural =  ['money','news', 'advice']

def plural(noun):
    if noun in no_plural:
        form = noun
    elif noun in noun_exceptions:
        form = noun_exceptions[noun]
    elif noun[-2:] in ['ch', 'sh']:
        form = noun + 'es'
    elif noun[-1:] in ['s', 'x', 'z']:
        form = noun + 'es'
    elif noun[-1:] == 'y':
        form = noun[:-1] + 'ies'
    else:
        form = noun + 's'
    return form




__author__ = 'ariyatan'

#the class takes a verb ('verb'), required tense ('tense') and person('person').
#In this case 'tense' means not only  common tenses, but also verb forms such as participle or adverb or gerund.
#'verb' is infinitive taken from vocabulary during previous stages
#'tense' is received from parser, and set to 'infinitive', if nothing is received.
#'person' is presumably received from parser, and set to 'you', if nothing is received.
#'person' can be 'I','you','she' (we try to be correct), 'we' or 'they'.
import csv

double_consonant_list = []
with open('verb_double_consonant.csv', 'rb') as dc:
    for line in dc:
        double_consonant_list.append(line[:-1])
        #I use [:-1] to get rid of '\n' symbol at the end of each row



class verb_form(object):
    def __init__(self, verb, tense = 'inf', person = 'you'):
        self.verb = verb
        self.tense = tense
        self.person = person

    def inf(self):
        return self.verb

    #nhave(self) is conjugation of the verb 'to have' to use it later as auxiliary verb
    def nhave(self):
        if self.person == 'she':
            return 'has'
        else:
            return 'have'

    #nbe(self) is conjugation of the verb 'to be' to use it later as auxiliary verb(present)
    def nbe(self):
        if self.person == 'I':
            return 'am'
        if self.person == 'she':
            return 'is'
        else:
            return 'are'

    #fbe(self) is conjugation of the verb 'to be' to use it later as auxiliary verb(future)
    def fbe(self):
        if self.person in ['I', 'we']:
            return 'shall'
        else:
            return 'will'

    #pbe(self) is conjugation of the verb 'to be' to use it later as auxiliary verb(past)
    def pbe(self):
        if self.person == 'she':
            return 'was'
        else:
            return 'were'


    def gerund(self):
        if self.verb == 'be':
            return 'being'
        elif self.verb[-1] == 'e':
            if self.verb in ['toe', 'singe', 'dye', 'see', 'agree', 'free', 'flee']:
                return self.verb + 'ing'
            if self.verb[-2] == 'ie':
                return self.verb[:-2] + 'ying'
            else:
                return self.verb[:-1] + 'ing'
        elif self.verb[-1] == 'c':
            return self.verb + 'ked'
        elif self.verb in double_consonant_list:
            return self.verb + self.verb[-1] + 'ing'

        else:
            return self.verb + 'ing'

    #ppl is passive participle
    def ppl(self):
        reader = csv.reader(open('verb_exceptions.csv'))
        verb_exceptions = {}
        for row in reader:
            key = row[0]
            verb_exceptions[key] = row[2]
        if self.verb in verb_exceptions.keys():
            return verb_exceptions[self.verb]
        elif self.verb == 'be':
            return 'been'
        elif self.verb[-1] == 'e':
            return self.verb + 'd'
        elif self.verb [-1] == 'y':
            if self.verb [-2] in ['ay', 'ey', 'oy', 'uy']:
                return self.verb + 'ed'
            else:
                return self.verb[:-1] + 'ied'
        elif self.verb[-1] == 'c':
            return self.verb + 'ked'
        elif self.verb in double_consonant_list:
            return self.verb + self.verb[-1] + 'ed'
        else:
            return self.verb + 'ed'

    def present_simple(self):
        if 'do' in self.verb:
            if self.person in ['I', 'you', 'we', 'they']:
                return self.verb
            if self.person == 'she':
                return 'does'
        elif 'be' in self.verb:
            if self.person == 'I':
                return 'am'
            if self.person == 'she':
                return 'is'
            else:
                return 'are'
        elif self.verb == 'have':
            return self.nhave()
        if 'she' in self.person:
            return self.verb + "s"
        else:
            return self.verb

    def present_continuous(self):
        return [self.nbe(), self.gerund()]

    def present_perfect(self):
        reader = csv.reader(open('verb_exceptions.csv'))
        verb_exceptions = {}
        for row in reader:
            key = row[0]
            verb_exceptions[key] = row[2]
        if self.verb in verb_exceptions.keys():
            return [self.nhave(), verb_exceptions[self.verb]]
        else:
            return [self.nhave(), self.ppl()]


    def past_simple(self):
        reader = csv.reader(open('verb_exceptions.csv'))
        verb_exceptions = {}
        for row in reader:
            key = row[0]
            verb_exceptions[key] = row[1]
        if self.verb in verb_exceptions.keys():
            return verb_exceptions[self.verb]
        elif self.verb == 'be':
            if self.person == 'she':
                return 'was'
            else:
                return 'were'
        else:
            return self.ppl()

    def future_simple(self):
        return [self.fbe(), self.verb]

    def past_perfect(self):
        return ['had', self.ppl()]

    def past_continuous(self):
        return [self.pbe(), self.gerund()]

    def future_continuous(self):
        return [self.fbe(), 'be' + ' ' + self.gerund()]

from adj_comparison import adj_form

#'0', 'pos' or 'positive' for positive; '1', 'com' or 'comparative' for comparative; '2', 'sup or 'superlative' for superlative



def adj_input():
    a_input = raw_input('Enter an adjective> \n')
    return a_input


def degree_input():
    degree = raw_input('Enter the required degree > \n')
    return degree

def form(adjective, case,  degree):
    if degree in ['positive', 'pos', '0']:
        return adjective
    if degree in ['comparative', 'com', '1']:
        return adj_form.comparative(case)
    if degree in ['superlative', 'sup', '2']:
        return adj_form.superlative(case)


#main

adjective = adj_input()
degree = degree_input()

case = adj_form(adjective, degree)

print form(adjective, case, degree)

while True:
    a = adj_input()
    if a != '':
        adjective = a

    d = degree_input()
    if d != '':
        degree = d

    if degree == '':
        degree = 'positive'
    else:
        pass

    case = adj_form(adjective, degree)

    print form(adjective, case, degree)

    print "\nLet's test some more"


#degree of comparison is used, if the qualities of different objects are compared. If the object is the same, it' just 'more',
#without synthetic forms: "Her eyes are more blue then gray", but "her eyes are bluer than Helena's"
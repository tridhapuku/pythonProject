#
# trans = input("enter a sentence ")
# trans = trans.upper()
#
# t_list = trans.split()
# acronym = ''
# for word in t_list:
#     acronym = acronym + word[0]
#     # print(word[0])
#
# # print('Acronym is {}'.format(acronym))
# print(acronym)

def acronym(trans):
    # trans = input("enter a sentence ")
    trans = trans.upper()

    t_list = trans.split()
    acronym = ''
    for word in t_list:
        acronym = acronym + word[0]
        # print(word[0])

    # print('Acronym is {}'.format(acronym))
    # print(acronym)
    return acronym

test1 = 'random access memory'
test2 = 'central process unit'

print(acronym(test1))
print(acronym(test2))

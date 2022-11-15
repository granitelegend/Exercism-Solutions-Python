
# How it works:
# iter1 = [1,2,a,b,3,4]
# iter2 = [12,a,b,3,4]
# iter5 = [12,a,b,34]

# Examples of working inputs:
# arg = ['1','2','a','b','3','4','5','c','',']']
# arg = [1,[2,355,5,None,4],[None],5,4,4,44]

def horrible_flatten_array(arg):
    """
    This flatten array function could be deemed 'horrible' due to its primitive method of flattening it.
    Function converts list -> string -> list, creating a large list, numbers that are close to each other are merged, -
    - and it is done this way to preserve numbers greater than 9 in the original list.
    Final step is removing all non-numbers in the list and returning it.
    :return:
    """

    arg = list(str(arg[:]))

    while ' ' in arg:
        arg.remove(' ')

    arg_numbers_only = []

    for x in arg:
        if x.isnumeric():
            arg_numbers_only.append(int(x))

    digit_list = list(range(0,max(arg_numbers_only)+1))
    digitsString = ''

    for x in digit_list:
        digitsString += str(x)

    digit_list = list(digitsString)

    pre_arg = 0
    post_arg = 1

    while pre_arg != post_arg:
        pre_arg = arg[:]
        new_number = ''
        for y in range(len(arg)):
            try:
                if (arg[y] in digit_list) and (arg[y+1] in digit_list):
                    new_number = arg[y] = arg[y] + arg[y+1]
                    arg.pop(y+1)
                    if not (new_number in digit_list):
                        digit_list.append(str(new_number))
                    else:
                        continue
                    break
                else:
                    continue
            except IndexError:
                break

        post_arg = arg[:]

    new_arg = []

    for x in arg:
        if x.isnumeric():
            new_arg.append(x)

    return new_arg


# ISBN Verifier
# Contains Verifier and Converter
# Notes:
# Conversion only works if the ISBN can be verified as True.

def isbn_verifier(isbn):
        """
        Takes ISBN-10 and -13 as input, returns True or False if the ISBN is valid.
        Function accepts both numbers only and with dashes.
        :param isbn: str
        :return: boolean
        """

        # ISBN-10 Verification

        isbn_dict = {}  # Used for smoother calculation regarding check digit
        isbn_digits_list = list(str(isbn))

        while '-' in isbn_digits_list:  # Remove dashes from list, for easier calculations
            isbn_digits_list.remove('-')

        counter_num = len(isbn_digits_list)  # Is used for if-statements to check what type of ISBN, -10 or -13
                                             # counter_num is used as a counting flag for loops and to check ISBN.
        if counter_num == 10:
            for x in isbn_digits_list:
                if x == 'X':
                    x = 10

                isbn_dict.update({counter_num:int(x)})  # Dictonary used for calculations, weights are generated -
                counter_num -= 1                        # - with the digits of the ISBN in format weight:digit.

            isbn_value = 0

            for x in isbn_dict:
                isbn_value += x*isbn_dict.get(x)

            return isbn_value % 11 == 0

        # ISBN-13 Verification
        # Uses same calculation method as before, but with tuples in a list instead.

        elif counter_num == 13:

            alternation_flag = 0
            operation_tuple_list = []
            for x in isbn_digits_list:  # For-loop alternates between to if-statements using alternation_flag.
                                        # alternation_flag shifts from 0 to 1, that is 0,1,0,1,0,1 etc.                                  #
                if counter_num == 1:
                    break

                if x.isnumeric() and alternation_flag == 0:
                    operation_tuple_list.append((1,int(x)))
                    counter_num -= 1
                    alternation_flag = 1
                    continue

                if x.isnumeric() and alternation_flag == 1:
                    operation_tuple_list.append((3,int(x)))
                    counter_num -= 1
                    alternation_flag = 0
                    continue


            isbn_value = 0

            for x,y in operation_tuple_list:
                isbn_value += x*y

            isbn_value = (10 - (isbn_value % 10))

            if isbn_value == 10:
                isbn_value = 0

            if int(isbn_value) == int(isbn_digits_list[-1]):
                return True
            else:
                return False


def isbn_converter(isbn):
    """
    Takes ISBN-10 and -13 as input (string) and converts it.
    ISBN-10 -> ISBN-13 and ISBN-13 -> ISBN-10.
    :param isbn: str
    :return: str
    """

    isbn_digits_list = list(str(isbn))

    while '-' in isbn_digits_list:
        isbn_digits_list.remove('-')

    counter_num = len(isbn_digits_list)

    if counter_num == 10 and isbn_verifier(isbn):  # ISBN-10 to ISBN-13, problem has

        counter_num = 12  # Repurpose variable for counting in algo

        isbn = "978-" + isbn[:]
        isbn = isbn[:-2]  # Remove Check-digit

        isbn_digits_list = list(str(isbn))

        alternation_flag = 0
        operation_tuple_list = []
        for x in isbn_digits_list:  # For-loop alternates between to if-statements using alternation flag

            if x.isnumeric() and alternation_flag == 0:
                operation_tuple_list.append((1, int(x)))
                counter_num -= 1
                alternation_flag = 1
                continue

            if x.isnumeric() and alternation_flag == 1:
                operation_tuple_list.append((3, int(x)))
                counter_num -= 1
                alternation_flag = 0
                continue

        isbn_value = 0

        for x, y in operation_tuple_list:
            isbn_value += x * y

        isbn_value = (10 - (isbn_value % 10))  # Check digit calculation
        if isbn_value == 10:
            isbn_value = 0
        isbn = isbn[:] + "-" + str(isbn_value)

        return isbn

    elif counter_num == 13 and isbn_verifier(isbn):  # ISBN-13 to ISBN-10

        if str(isbn[0:3]) == "978":

            isbn = isbn[4:-2]  # Remove "978" and check digit from ISBN string

            isbn_dict = {}
            isbn_digits_list = list(str(isbn))

            while '-' in isbn_digits_list:
                isbn_digits_list.remove('-')

            counter_num = 10

            if counter_num == 10:
                for x in isbn_digits_list:
                    if x == 'X':
                        x = 10

                    isbn_dict.update({counter_num: int(x)})
                    counter_num -= 1

                isbn_value = 0
            for x in isbn_dict:
                isbn_value += x * isbn_dict.get(x)

            if (11 - isbn_value % 11 == 10): # Check digit
                return isbn + "-0"
            else:
                return isbn + "-" + str(11 - isbn_value % 11)
        else:
            print("ISBN can't be converted")

    else:
        print("Invalid input")





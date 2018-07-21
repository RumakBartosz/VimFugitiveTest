
text_file = open("data", "r")
data = text_file.read().split('\n')


def dot_input(input):
    return '.' + input + '.'


def unnumerator(word):
    ret_word = ""
    for element in word:
        if not element.isdigit():
            ret_word += element

    return ret_word


def unnumerator_looper(data):
    unnumered_data = []
    for index, element in enumerate(data):
        unnumered_data.append(unnumerator(element))
    return unnumered_data


def lists_to_dictionary(list1, list2):
    return dict(zip(list1, list2))


def compare_dict_to_string(string1, dict1):     # uogolnij na 2d list, gdy
                                                # znajdzie
                                                # wstaw od pozycji na ktorej
                                                # znalazl, wymiar 2 w dol
    for key, element in dict1.items():
        if string1.find(element) != -1\
                and len(key) > 0:
            if not string1[string1.find(element) - 1].isdigit()\
                    and not string1[string1.find(element)
                                    + len(element) - 1].isdigit():
                string1 = string1.replace(element, key)
    return string1


def hyphenate(string1):
    hyphenated_string = ""
    returned_string = ""
    for index, element in enumerate(string1):
        if element.isdigit() and int(element) % 2\
                and index != 0 and index != len(string1):
            hyphenated_string += '-'
        elif element.isdigit():
            continue
        else:
            hyphenated_string += element
    returned_string = hyphenated_string[1:-1]
    return returned_string


# main = dot_input(text_file)
# -> unnumered_text_file = unnumerator_looper(text_file)
# -> dict_data = list_to_dictionary(text_file,unnumered_text_file)
# -> numered_string = compare_dict_to_string("cos",dict_data)
# -> hyphenate(numered_string)

string_test = dot_input("recursion")

unnumered_text_file = unnumerator_looper(data)

dict_data = lists_to_dictionary(data, unnumered_text_file)

numered_string = compare_dict_to_string(string_test, dict_data)
# print(dict_data)
# print(numered_string)
print(hyphenate(numered_string))

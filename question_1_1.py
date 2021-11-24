def unique_char(string):
    dict = {}
    for i in string:
        if i in dict:
            return False

        else: 
            dict[i] = 1
    return True
    


print(unique_char("abcd"))
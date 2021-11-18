from typing import final


def string_compression(str1):
    str_d = {}
    final_str = ""
    for i in range(len(str1)):

        if(str1[i] in str_d): str_d[str1[i]] +=1 
        else:
            str_d[str1[i]] = 1 
        if(i == len(str1)-1):
            final_str += str1[i]
            final_str += str(str_d[str1[i]])
            del str_d[str1[i]]
            break
        if(str1[i+1] != str1[i]):
            final_str += str1[i]
            final_str += str(str_d[str1[i]])
            del str_d[str1[i]]

    return final_str



print(string_compression("aabcccccaaa"))
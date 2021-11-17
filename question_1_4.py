def palindrome_perm(str):
    str = str.lower()
    str_d = {}
    length_str = 0
    for i in str:
        if(i == ' '):
            continue
        length_str  += 1
        if i in str_d:
            str_d[i] +=1
        else: 
            str_d[i] = 1
    print(str_d)
    num_of_odd = 0

    for i in str_d.keys():
        if(str_d[i] % 2 == 1):
            num_of_odd +=1
        else:
            continue
    if(length_str % 2 == 1):
        if num_of_odd > 1:
            return False
    else:
        if num_of_odd > 0:
            return False

    return True


print(palindrome_perm("Tact Coa"))
def check_perm(str1, str2):
    str1_d = {}
    for i in str1:
        if i in str1_d:
            str1_d[i] += 1
        else:
            str1_d[i] = 1 
    
    for b in str2:
        if b not in str1_d:
            return False
        else:
            str1_d[b] -=1
    
    for i in str1_d.keys():
        if(str1_d[i] < 0 or str1_d[i] > 0):
            return False

    return True

print(check_perm("abcad", "cbaa"))
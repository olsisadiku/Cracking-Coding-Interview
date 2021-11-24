def isSubstring(s1,s2):
    if(len(s1) != len(s2)):
        return False

    amount_checked = 0
    index_s1 = 0
    index_s2 = 0
    runner = 0
    while index_s1 < len(s1) or runner > len(s1) or amount_checked == len(s1)-1:
        
        if(s1[index_s1] == s2[index_s2 % len(s1)]):
            amount_checked += 1
            index_s2 = (index_s2 + 1)  % len(s1)
            index_s1 += 1 
        else:
            amount_checked = 0 
            index_s2 = (index_s2 + 1) % len(s1)
            runner += 1 
        
    if(amount_checked == len(s1)):
        return True
    return False



print(isSubstring("waterbottle", "ttlewaterbo"))
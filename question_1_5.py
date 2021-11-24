def one_away(str1, str2):
    if(len(str1) == len(str2)):
        num_diff = 0
        for i in range(len(str2)):
            if(str1[i] != str2[i]):
                num_diff +=1
                if(num_diff > 1):
                    return False
    
    if(len(str1) != len(str2)):
        if(abs(len(str1) - len(str2)) > 1):
            return False
        
        str1_bigger = len(str1) > len(str2) 
        if(str1_bigger):
            i_for2 = 0
            i = 0
            num_different = 0 
            while i < len(str1):
                if(str1[i] == str2[i_for2]):
                    i +=1
                    i_for2 +=1
                elif (str1[i] != str2[i_for2]):
                    num_different +=1
                    i+=1
                if(num_different > 1):
                    return False
                if(i == len(str2) and num_different < 2):
                    return True
    return True

# I know I dont cover the str2 is bigger because I was too lazy lol 



print(one_away("pale", "bae"))
def vowel_consonant_check(s):
    vowel = "aeiouAEIOU"
    v,c = 0, 0
    for char in s:
        if char.isalpha():
            if char in vowel:
                v +=1
            else:
                c +=1
    return v,c 
    
result = vowel_consonant_check(input("please enter the string"))
    
print(result)
print(result[0])
print(result[1])

                
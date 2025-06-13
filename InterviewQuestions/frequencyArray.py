def frequency_function(s):
    count_num = {}
    for i in s:
        if i in count_num:
            count_num[i] += 1 
        else:
            count_num[i] = 1 
    
    return count_num
            
s = [1,3,4,5,6,1,2,4,5,3]
print(frequency_function(s))
            
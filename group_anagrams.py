def group_anagrams(strings):
    #write your code here
    if len(strings)==0:
        return []
        
    sorted_string = [''.join(sorted(i)) for i in strings]
    
    hash={}
    
    for i in range(len(sorted_string)):
        if(sorted_string[i] in hash):
            hash[sorted_string[i]].append(strings[i])
        else:
            hash[sorted_string[i]]=[strings[i]]
        
    return list(hash.values())
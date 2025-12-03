

# checking anagrams using the "sort" built-in function.
'''
def anagrams_checker(s1,s2):
    return sorted(s1.replace(" "," ").lower())== sorted(s2.replace(" "," ").lower())
print(anagrams_checker("hello","World"))
'''


##checking the anagrams without using the built-in function 
def is_anagram(s1,s2):
    s1 = s1.replace(" ","").lower()
    s2 = s2.replace(" ","").lower()

    if(len(s1)!=len(s2)):
        return False
    
    freq1 = [0]*26
    freq2 = [0]*26
    
    for ch in s1:
        freq1[ord(ch)- ord('a')] += 1
    for ch in s2 :
        freq2[ord(ch)- ord('a')] += 1

    return freq1==freq2
print(is_anagram("listen","silent"))
print(is_anagram("hello","world"))

def vowels_constants(n):
    vowel_counts = 0
    constants_counts =0
    vowels="aeiouAEIOU"
    for w in n:
       if w.isalpha(): #ensures digits, spaces, and symbols are ignored
        if w in 'aeiouAEIOU':
            vowel_counts = vowel_counts+1
        else:
            constants_counts = constants_counts+1
    print("the total vowel counts are:", vowel_counts)
    print("the total constants are:",constants_counts)


n = str(input("enter the string"))
print(vowels_constants(n))

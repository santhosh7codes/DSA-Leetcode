def isAnagram(a, b):
    if len(a) != len(b):
        return False
    count = {}
    for ch in a:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1
    for ch in b:
        if ch not in count:
            return False
        count[ch] -= 1
        if count[ch] < 0:
            return False
    return True
a = input("Enter the first string ")
b = input("Enter the second string ")

if isAnagram(a, b):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    # word = list(word)
    # word.sort()
    # anagram = list(anagram)
    # anagram.sort()

    if sorted(word) == sorted(anagram):
        return True
    else:   
        return False 
    
   #calling the function
find_anagram("below", "elbow")
find_anagram("hello", "check")
find_anagram("python", "typhon")

print(find_anagram("below", "elbow"))
print(find_anagram("hello","check"))
print(find_anagram("python", "typhon"))




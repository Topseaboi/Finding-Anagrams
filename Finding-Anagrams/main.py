# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    if word.lower() == anagram.lower():
        return False
    word = len(word)
    anagram = len(anagram)
    check_len = word == anagram
    #checking1=sorted(list(word.lower()))
    #checking2=sorted(list(anagram.lower()))
    #checked= checking1 == checking2
    return check_len #and checked

print (find_anagram("beats", "beast"))

print (find_anagram("listen", "silent"))

print (find_anagram("badd", "dwand"))


def isPalindrom(word):
    """
    isPalindrom checks if provided by user word is palindorm 
    return True if word is a palindrom 
    return False if word isn't a palindrom
    Argument:
    word
    """
    i=0
    for letter in word:
        if letter != word[len(word)-i-1]:
            return False;
        i+=1
    return True;

print("kajaki " + str(isPalindrom("kajaki")))
print("kajak " + str(isPalindrom("kajak")))  
print("potok " + str(isPalindrom("potok")))
print("potop " + str(isPalindrom("potop")))  
print(help(isPalindrom))         
def even_min(num1,num2):
    
    if num1 % 2 == 0 and num2 % 2 == 0:
        return min(num1, num2)
    else:
        return max(num1, num2)
            
def even_cap(word):
    
    new_word = ''
    lenght=len(word)
    print(lenght)
    for num in range (0, lenght):
        if num % 2 == 0:
            new_word = new_word + word[num].lower()
        else:
            new_word = new_word + word[num].upper()
            
    return new_word

def animal_cracker(word1):
    
    wordlist = word1.split()
    return wordlist[0].lower()[0] == wordlist[1].lower()[0]
        
# Driver program to test
print(even_min(2, 2))
print(even_cap('AvikDebAyutasOurideb'))
print(animal_cracker("Long lion"))        

    
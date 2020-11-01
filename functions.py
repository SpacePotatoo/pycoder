"""
@Author: Ayuta
Description: a LOT of functions
Input:
Output:
"""

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

def makes_20(num1,num2):
    if num1 + num2 == 20 or num1 == 20 or num2 ==20 :
        return True    

    else:
        return False
    
def capitalize_data(word2):
    s1 = word2[0].capitalize()
    s2 = word2[1:3] 
    s3 = word2[3].capitalize()
    s4 = word2[4:]    
    return s1+s2+s3+s4
    
def master_yoda(sentence):
    sent_list = sentence.split()
    sent_list.reverse()
    return ' '.join(sent_list)
    
    
# Driver program to test
print(even_min(2, 2))
print(even_cap('AvikDebAyutasOurideb'))
print(animal_cracker('Long lion'))  
print(makes_20(16, 20))
print(capitalize_data('gurgaon'))
print(master_yoda('my name is ayuta')) 
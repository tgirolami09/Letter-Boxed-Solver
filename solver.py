from functions import *

with open(usablePath("./letter_boxed_words.txt"),"r") as file:
    words=file.read().splitlines()

alphabet = set("abcdefghijklmnopqrstuvwxyz")
attached_sides:list[str] = []
sides = {}

for loop in range(4):
    i = input("Give me the 3 letters of a side : ").strip()
    alphabet-=set(i)
    attached_sides+=list(i)
    for char in i:
        sides[char]=set(i)-set(char)
    
alphabet = sorted(list(alphabet))
valid_words = []
valid_words_by_first_letter = {letter:[] for letter in attached_sides}

for word in words:
    if set(word)-set(attached_sides):
        pass
    else:
        for index,char in enumerate(word[:-1]):
            if word[index+1] in sides[char]:
                break
        else:
            valid_words.append(word)
            valid_words_by_first_letter[word[0]].append(word)

minimalWordSolutions(valid_words,valid_words_by_first_letter)

user_input = ""
while user_input!="#stop":
    user_input=input("Give me a word if its unvalid ot write '#stop' to stop : ").strip().lower()
    if user_input=="#stop":
        break

    elif valid_words.count(user_input)!=0:
        valid_words.remove(user_input)
        valid_words_by_first_letter[user_input[0]].remove(user_input)
        print(f"Removed the word '{user_input}' on this execution, it has not been removed from the word list")

    else:
        print(f"The word '{user_input}' is not in my current list")

    minimalWordSolutions(valid_words,valid_words_by_first_letter)
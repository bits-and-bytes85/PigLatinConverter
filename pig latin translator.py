

original = input("What would you like to translate : ").strip().lower()


#split sentence
words = original.split()

# loop and convert to pig latin
new_words = []


# if it starts with a vowel, add "yay" to the end
for word in words:
    if word[0] in "aeiou":
        new_word = word + "yay"
        new_words.append(new_word)
    else: # Checks when vowels stop
        vowel = 0
        for letter in word:
            if letter not in "aeiou":
                vowel = vowel + 1
            else:
                break
        cons = word[:vowel]
        the_rest = word[vowel:]
        new_word = the_rest + cons + "ay"
        new_words.append(new_word)

# stick words back together with correct formatting

output = " ".join(new_words)
print(output)

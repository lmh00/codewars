def vowel_indices(word):
    vowels = ["a", "e", "i", "o", "u", "y"]
    word = word.lower()
    output = []

    for i in range(len(word)):
        if word[i] in vowels:
            output.append(i + 1)

    print(output)


vowel_indices("mmm")  # []
vowel_indices("apple") # [1,5]
vowel_indices("123456") # []
vowel_indices("UNDISARMED") # [1,4,6,9]
vowel_indices("supercalifragilisticexpialidocious")

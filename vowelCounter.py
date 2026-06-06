counting_vowels = input("Give a word: ")
vowels_low = "aeiou"
vowels_upper = "AEIOU"

letterCounting_lower = sum(1 for search in counting_vowels if search in vowels_low)
letterCounting_upper = sum(1 for search in counting_vowels if search in vowels_upper)

print(f"{letterCounting_lower} lowercase")
print(f"{letterCounting_upper} UpperCase")

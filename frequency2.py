test_dict = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}

print("Dictionary : ",test_dict)

freq_word = input("enter the word to check its frequency: ")

# Print the frequency
if freq_word in test_dict:
    print("Frequency of ",freq_word," is : ",test_dict[freq_word])
else:
    print(freq_word, "is not present in the dictionary.")
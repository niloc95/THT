### Instructions - 

Prerequisites
Python 3.x installed on your system
Visual Studio Code installed on your system



### Worst-case Space Complexity Analysis

The numeral_to_words function uses a dictionary to map digits to their corresponding words. The size of the 
dictionary is constant, so the space complexity of the dictionary is O(1).

The numeral_to_words function uses a dictionary to map digits to their corresponding words, but this dictionary takes up a constant amount of space that doesn't change based on the input number.

The function also uses a list to store the words that make up the standard way of reading the number. The longer the input number, the longer the list will be. For example, if the input number is 999, the list will contain 3 words. If the input number is 123456789, the list will contain 5 words. The space taken up by this list grows in proportion to the length of the input number.

Finally, the function concatenates the words in the list into a string that includes spaces and punctuation. The length of this string is also proportional to the length of the input number.

Overall, the amount of space used by the numeral_to_words function grows linearly with the length of the input number. This is reasonable for most practical purposes, and it means that the function won't use up an unreasonable amount of memory even for very large input numbers.
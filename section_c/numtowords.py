#def test_numeral_to_words():
    # Test cases go here
    #assert numeral_to_words('0') == 'Zero.'
#if __name__ == '__main__':
    # Run the test suite
#    test_numeral_to_words()


def numeral_to_words(numeral):
    """
    Converts a numeral to its standard way of reading a number.
    
    Parameters:
        numeral (str): A numeral represented as a string of digits without separators.
    
    Returns:
        str: The standard way of reading the number represented by the numeral,
             with appropriate punctuation.
    """
    # Define a list of words for each digit
    digit_words = [
        'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'
    ]
    # Define a list of words for each ten-digit combination
    ten_words = [
        '', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'
    ]
    # Define a list of words for each two-digit combination
    teen_words = [
        'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
        'seventeen', 'eighteen', 'nineteen'
    ]
    # Convert the numeral to a string and split it into groups of three digits
    groups = []
    while numeral:
        groups.append(numeral[-3:])
        numeral = numeral[:-3]
    # Convert each group to words and concatenate them with appropriate commas and conjunctions
    words = []
    for i, group in enumerate(reversed(groups)):
        group_words = []
        if len(group) == 3:
            if group[0] != '0':
                group_words.append(digit_words[int(group[0])] + ' hundred')
            group = group[1:]
        if len(group) == 2:
            if group[0] == '1':
                group_words.append(teen_words[int(group[1])])
            else:
                if group[0] != '0':
                    group_words.append(ten_words[int(group[0])])
                if group[1] != '0':
                    group_words.append(digit_words[int(group[1])])
        elif len(group) == 1:
            if group[0] != '0' or (i == 0 and not words):
                group_words.append(digit_words[int(group[0])])
        if group_words:
            if i == 0:
                words.extend(group_words)
            elif i == 1:
                words.extend(group_words + ['thousand'])
            elif i == 2:
                words.extend(group_words + ['million'])
            elif i == 3:
                words.extend(group_words + ['billion'])
            else:
                words.extend(group_words + ['trillion'])
    # Return the concatenated words with the appropriate punctuation
    if not words:
        return 'zero'
    elif len(words) == 1:
        return words[0].capitalize()
    else:
        return ' '.join(words[:-1]).capitalize() + ' and ' + words[-1] + '.'

# Ask the user for a numeral and convert it to the standard way of reading a number
numeral = input('Please enter a numeral (just digits without separators): ')
words = numeral_to_words(numeral)
print(words)

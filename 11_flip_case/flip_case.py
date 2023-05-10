def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    # new = ""

    # for letter in phrase:
    #     if letter == to_swap:
    #         if letter.isupper():
    #             letter.lower()
    #         else: letter.upper()
    #     new += letter

    #     return new

    to_swap = to_swap.lower()
    out = ""

    for ltr in phrase: 
        if ltr.lower() == to_swap:
            ltr = ltr.swapcase()
        out += ltr
    
    return out
        
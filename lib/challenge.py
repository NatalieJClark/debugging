# CHALLENGE: Debug this program ...
# def get_most_common_letter(text):
#     counter = {}
#     for char in text:
#         counter[char] = counter.get(char, 0) + 1
#     letter = sorted(counter.items(), key=lambda item: item[1])[0][1]
#     return letter


# print(f"""
# Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
# Expected: o
# Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
# """)

# SOLUTION:
def get_most_common_letter(text):
    counter = {}
    for char in text:
        #  For any alphabet letters in text, create a dictionary with:
        #  key = alphabet letter in text
        #  value = number of times the alphabet letter occurs in text
        if char.isalpha():
            counter[char] = counter.get(char, 0) + 1
    #  Turn the dictionary into a list of tuples
    #  Sort this list in acsending order of the tuple index 1 values
    #  Return the zero index of the final tuple in the list, to give the most common letter in text
    letter = sorted(counter.items(), key=lambda item: item[1])[-1][0]
    return letter


print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")
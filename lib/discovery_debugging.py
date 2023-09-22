def encode(text, key):
    # Create cipher list using keyword
    cipher = make_cipher(key)
    ciphertext_chars = []
    for i in text:
        # For each letter in given text, find the index of that letter within the cipher list
        # Add 65 to this index number
        # Use the resulting unicode to generate a ciphered character
        ciphered_char = chr(65 + cipher.index(i))
        #  Add the ciphered character to a list
        ciphertext_chars.append(ciphered_char)
    #  Return the list of ciphered characters as a joined string
    return "".join(ciphertext_chars)


def decode(encrypted, key):
    # Create cipher list using keyword
    cipher = make_cipher(key)
    plaintext_chars = []
    for i in encrypted:
        #  For each letter in the given encrypted text, turn the letter into a unicode number
        #  Minus 65 from this number
        #  Use the result as an index to find a deciphered letter in the cipher list
        plain_char = cipher[ord(i) - 65]
        plaintext_chars.append(plain_char)

    return "".join(plaintext_chars)


def make_cipher(key):
    #  Create list of alphabet characters
    alphabet = [chr(i + 96) for i in range(1, 27)]
    # Add the alphabet list to the end of a list of the characters in the keyword
    cipher_with_duplicates = list(key) + alphabet

    cipher = []
    for i in range(0, len(cipher_with_duplicates)):
        #  Remove any duplicated characters from the list to create the cipher list
        if cipher_with_duplicates[i] not in cipher_with_duplicates[:i]:
            cipher.append(cipher_with_duplicates[i])
    return cipher

# When you run this file, these next lines will show you the expected
# and actual outputs of the functions above.
print(f"""
 Running: encode("theswiftfoxjumpedoverthelazydog", "secretkey")
Expected: EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL
  Actual: {encode('theswiftfoxjumpedoverthelazydog', 'secretkey')}
""")

print(f"""
 Running: decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey")
Expected: theswiftfoxjumpedoverthelazydog
  Actual: {decode('EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL', 'secretkey')}
""")
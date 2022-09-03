# Caesar Cipher
# https://www.nostarch.com/crackingcodes (BSD Licensed)
# the code was modified by me

import pyperclip

# The string to be encrypted/decrypted:
message = 'This is my secret message.'

# The encryption/decryption key:
key = 13

# Whether the program encrypts or decrypts:
mode = 'encrypt'  # Set to either 'encrypt' or 'decrypt'.

# Every possible symbol that can be encrypted:
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'


# Stores the encrypted/decrypted form of the message:

def cezar_make(SYMBOLS, message, key, mode) -> 'str':
    translated = ''
    for symbol in message:
        # Note: Only symbols in the `SYMBOLS` string can be encrypted/decrypted.
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)

            # Perform encryption/decryption:
            if mode == 'encrypt':
                translatedIndex = symbolIndex + key
            elif mode == 'decrypt':
                translatedIndex = symbolIndex - key

            # Handle wrap-around, if needed:
            if translatedIndex >= len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            translated = translated + SYMBOLS[translatedIndex]
        else:
            # Append the symbol without encrypting/decrypting:
            translated = translated + symbol
    return translated


# Output the translated string:
# res = cezar_make(SYMBOLS,message,key, mode)
# print(res)
# pyperclip.copy(res)
# print(__name__)

def main() -> 'none':
    res = cezar_make(SYMBOLS, message, key, mode)
    print(res)
    pyperclip.copy(res)

if __name__ == '__main__':
    main()


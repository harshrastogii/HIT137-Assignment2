# function to only read text file
def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.read()

# function to write content in text file
def write_file(file_name, content):
    with open(file_name, 'w') as file:
        file.write(content)

# function to shift characters with in range 
def shift_char_within_range(char, start, end, shift):
    return chr((ord(char) - ord(start) + shift) % (ord(end) - ord(start) + 1) + ord(start))

# function for the encryption process
def encrypt(text, n, m):
    encrypted_text = ""
    for char in text:
        if 'a' <= char <= 'm':
            encrypted_text += shift_char_within_range(char, 'a', 'm', n * m)
        elif 'n' <= char <= 'z':
            encrypted_text += shift_char_within_range(char, 'n', 'z', -(n + m))
        elif 'A' <= char <= 'M':
            encrypted_text += shift_char_within_range(char, 'A', 'M', -n)
        elif 'N' <= char <= 'Z':
            encrypted_text += shift_char_within_range(char, 'N', 'Z', m ** 2)
        else:
            encrypted_text += char  # this is for the number and other special character
    return encrypted_text

# function for decryption process
def decrypt(text, n, m):
    decrypted_text = ""
    for char in text:
        if 'a' <= char <= 'm':
            decrypted_text += shift_char_within_range(char, 'a', 'm', -(n * m))
        elif 'n' <= char <= 'z':
            decrypted_text += shift_char_within_range(char, 'n', 'z', n + m)
        elif 'A' <= char <= 'M':
            decrypted_text += shift_char_within_range(char, 'A', 'M', n)
        elif 'N' <= char <= 'Z':
            decrypted_text += shift_char_within_range(char, 'N', 'Z', -(m ** 2))
        else:
            decrypted_text += char  # this is for the number and other special character
    return decrypted_text

# function to check correctness of decryption
def check_correctness(original, decrypted):
    return original == decrypted

# user input 
n = int(input("Enter value for n: "))
m = int(input("Enter value for m: "))

# read raw text using read_file function
raw_text = read_file('raw_text.txt')

# encryption of the text
encrypted_text = encrypt(raw_text, n, m)
write_file('encrypted_text.txt', encrypted_text)

# decryption of the text
decrypted_text = decrypt(encrypted_text, n, m)
write_file('decrypted_text.txt', decrypted_text)

# check if original text and decrypted text matches
if check_correctness(raw_text, decrypted_text):
    print("Decryption is correct")
    print("Decrypted text saved to 'decrypted_text.txt'")
else:
    print("Decryption is incorrect")

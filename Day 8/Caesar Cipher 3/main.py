





from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(direction1, shift_amount):

    if direction1 == "encode":
        def encrypt(original_text, shift_amount1):
            cipher_text = ""
            for letter in original_text:
                if letter in alphabet:
                    shifted_position = alphabet.index(letter) + shift_amount1
                    shifted_position %= len(alphabet)
                    cipher_text += alphabet[shifted_position]
                elif letter not in alphabet:
                    cipher_text += letter
            print(f"Here is the encoded result: {cipher_text}")
        encrypt(text, shift_amount)
    elif direction1 == "decode":
        def decrypt(original_text, shift_amount2):

            decrypted_text = ""
            for letter in original_text:
                if letter in alphabet:
                    reversed_position = alphabet.index(letter) - shift_amount2
                    reversed_position %= len(alphabet)
                    decrypted_text += alphabet[reversed_position]
                elif letter not in alphabet:
                    decrypted_text += letter
            print(f"Here is the decoded result: {decrypted_text}")
        decrypt(text, shift_amount)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
caesar(direction, shift)
restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'\n").lower()
while restart == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction, shift)
    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'\n").lower()
print("Goodbye!")


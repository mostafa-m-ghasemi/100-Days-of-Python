alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



# def encrypt (original_text, shift_amount):
#     cipher_text = ""
#     for i in original_text:
#         shifted_position = alphabet.index(i) + shift_amount
#         shifted_position %= len(alphabet)
#         cipher_text += alphabet[shifted_position]
#     print(f"Encode result: {cipher_text}")

# def decrypt (original_text, shift_amount):
#     cipher_text = ""
#     for i in original_text:
#         shifted_position = alphabet.index(i) - shift_amount
#         shifted_position %= len(alphabet)
#         cipher_text += alphabet[shifted_position]
#     print(f"Decode result: {cipher_text}")

def caesar(original_text, shift_amount, encode_or_decode):
    output = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for i in original_text:
        if i not in alphabet:
            output += i
        else:
            shifted_position = alphabet.index(i) + shift_amount
            shifted_position %= len(alphabet)
            output += alphabet[shifted_position]
    print(f"{encode_or_decode}d result: {output}")

should_continue = True
while should_continue:
    direction = input("would you like to encode or decode?\n").lower()
    text = input("what is your text?\n").lower()
    shift = int(input("how many letters would you like to shift?\n"))
    caesar(text, shift, direction)
    restart = input("would you like to continue? \n").lower()
    if restart == "no":
        should_continue = False
    print("*" * 5, "Good bye!", "*" * 5)

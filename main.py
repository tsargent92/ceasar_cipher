import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encryption(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter in alphabet:
            shifted_position = (alphabet.index(letter) + shift_amount) % 26
            output_text += alphabet[shifted_position]
        else:
            output_text += letter
    print(f"Here is the {encode_or_decode}d result: {output_text}")

machine_on = True
while machine_on:
    # Validate 'encode' or 'decode'
    direction = input("Type 'encode' to encrypt, or 'decode' to decrypt:\n").lower()
    if direction not in ['encode', 'decode']:
        print("Invalid choice. Please type 'encode' or 'decode'.")
        continue

    text = input("Type your message:\n").lower()

    # Validate that shift is a number
    try:
        shift = int(input("Type the shift number:\n"))
        shift %= 26
    except ValueError:
        print("Invalid shift. Please enter a number.")
        continue

    encryption(original_text=text, shift_amount=shift, encode_or_decode=direction)

    # Validate restart input
    while True:
        restart = input("Type 'yes' to go again, or 'no' to quit:\n").lower()
        if restart == "yes":
            break
        elif restart == "no":
            machine_on = False
            print(art.goodbye)
            break
        else:
            print("Invalid input. Please type 'yes' or 'no'.")
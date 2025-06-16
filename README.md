Caesar Cipher Encoder/Decoder
A clean, terminal-based Caesar Cipher app written in Python. This project allows users to encode or decode messages using a classic letter-shifting cipher with proper input validation and stylized ASCII art banners.

- Files
main.py – Main application logic and interactive loop.

art.py – Contains the logo and exit messages as multi-line ASCII art.

- Features
Encode and decode messages using Caesar cipher logic

Keeps non-alphabetic characters unchanged (e.g., numbers, punctuation)

Handles invalid inputs gracefully (e.g., typing "three" instead of 3)

Wraps shifts beyond 26 letters (e.g., a shift of 52 = shift of 0)

ASCII art banners for startup and exit (adds flavor!)

Restart the program as many times as you'd like without relaunching

- How to Use
Type 'encode' to encrypt, or 'decode' to decrypt:
> encode
Type your message:
> hello world!
Type the shift number:
> 5
Here is the encoded result: mjqqt btwqi!

Type 'yes' to go again, or 'no' to quit:
> no
<Goodbye>

- What is the Caesar Cipher?
A Caesar Cipher shifts each letter in the message by a fixed number. For example, a shift of 3 turns:

a → d

b → e

...

z → c (wraps around)

It’s one of the simplest and oldest encryption techniques in history.

- Future Ideas
Add uppercase letter support
Allow multi-language character sets
Include a “crack mode” to brute-force decode messages
GUI version with tkinter

- Author
This project was created by Tim Sargent using Angela Yu’s Caesar Cipher as the foundation. Extended and customized with error handling, repeatable input loops, and ASCII art banners.

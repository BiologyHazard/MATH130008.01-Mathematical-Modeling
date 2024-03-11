from string import ascii_uppercase, ascii_lowercase


def caesar_cipher(text: str, shift: int) -> str:
    result: list[str] = []
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += ascii_uppercase[(ascii_uppercase.index(char) + shift) % 26]
            else:
                result += ascii_lowercase[(ascii_lowercase.index(char) + shift) % 26]
        else:
            result += char
    return ''.join(result)


def format_output(text: str, n: int) -> str:
    return ' '.join([text.replace(' ', '')[i:i + n] for i in range(0, len(text), n)])


plain_text = "FUDAN UNIVERSITY"
cipher_text = caesar_cipher(plain_text, 12)
cipher_text_formatted = format_output(cipher_text, 5)

print(f"Plain text: {plain_text}")
print(f"Cipher text: {cipher_text_formatted}")

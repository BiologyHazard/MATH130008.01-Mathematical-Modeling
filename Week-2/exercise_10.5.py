from string import ascii_uppercase

import numpy as np


def hill_encrypt_group(text: str, key: np.ndarray) -> str:
    group = np.array([ascii_uppercase.index(char) for char in text])
    result = key @ group % 26
    return ''.join([ascii_uppercase[i] for i in result])


def hill_encrypt(text: str, key: np.ndarray, n: int) -> str:
    groups = [text[i:i+n] for i in range(0, len(text), n)]
    if len(groups[-1]) < n:
        import random
        groups[-1] += ''.join(random.choices(ascii_uppercase, k=n - len(groups[-1])))
    return ' '.join([hill_encrypt_group(group, key) for group in groups])


N = 3

A = np.array(
    [[1, 2, 4],
     [4, 7, 6],
     [6, 10, 5]]
)

B = np.array(
    [[1, 2, 3],
     [4, 6, 7],
     [5, 2, 3]]
)

det_A = round(np.linalg.det(A))
det_A_mod_26 = det_A % 26
det_B = round(np.linalg.det(B))
det_B_mod_26 = det_B % 26

print(f'det(A) = {det_A_mod_26} (mod 26)')
print(f'det(B) = {det_B_mod_26} (mod 26)')

# >>> det(A) = 25 (mod 26)
# >>> det(B) = 10 (mod 26)


text = "CRYPTOGRAPHY"
cipher_text_A = hill_encrypt(text, A, N)
print(f"Plain text: {text}")
print(f"Cipher text (A): {cipher_text_A}")

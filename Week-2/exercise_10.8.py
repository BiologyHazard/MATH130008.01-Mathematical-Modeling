from string import ascii_uppercase

p = 19
q = 31
public_key = (527, 589)
cipher_text = "04926 44064 06010"

phi_n = (p - 1) * (q - 1)
e, n = public_key
d = pow(e, -1, phi_n)
plain_text = ''.join(ascii_uppercase[pow(int(group), d, n)]
                     for group in ['049', '264', '406', '406', '010'])
print(f"Plain text: {plain_text}")

# >>> Plain text: HELLO

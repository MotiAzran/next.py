import string

password = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"
to = ''.join([chr(((ord(c) - ord('a') + 2) % 26) + ord('a')) for c in string.ascii_lowercase])

# print(''.join([chr(((ord(c) - ord('a') + 2) % 26) + ord('a')) if c.isalpha() else c for c in password]))
print(password.translate(string.maketrans(string.ascii_lowercase, to)))

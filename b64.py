from base64 import b64encode

filename = "widgets/home.png"
print(filename + ':', b64encode(open(filename, 'rb').read()))

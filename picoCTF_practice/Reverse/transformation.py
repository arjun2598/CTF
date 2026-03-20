with open("enc", "r") as f:
    text = f.read()

res = ""
for s in text:
    first = chr(ord(s) >> 8)
    res += first

    second = chr(ord(s) - (ord(first) << 8))
    res += second

print(res)
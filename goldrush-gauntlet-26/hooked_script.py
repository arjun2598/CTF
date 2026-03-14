text = '''Row 103: sc across
Row 103: sc across
Row 99: sc across
Row 116: sc across
Row 102: sc across
Row 123: sc across
Row 99: sc across
Row 114: sc across
Row 111: sc across
Row 99: sc across
Row 104: sc across
Row 101: sc across
Row 116: sc across
Row 95: sc across
Row 99: sc across
Row 105: sc across
Row 112: sc across
Row 104: sc across
Row 101: sc across
Row 114: sc across
Row 125: sc across'''

vals = []
l = 0
while l < len(text):
    num = ""
    while text[l].isdigit():
        num += text[l]
        l += 1
    
    if len(num) > 0:
        vals.append(int(num))
    else:
        l += 1

print(vals)

res = ""
for val in vals:
    res += chr(val)

print(res)
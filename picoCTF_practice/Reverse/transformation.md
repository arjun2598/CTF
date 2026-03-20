# Transformation

## Challenge

I wonder what this really is...
enc ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

`enc` is a text file containing the following: `灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸形㝦㘲捡㕽`

## Approach

1. First, we need to understand what the code described is doing. Essentially, it is taking every two characters from the flag, and then it is adding the ASCII value of the second character with the ASCII value of the first character shifted left by 8 bits.

2. Therefore, we just need to reverse the operation to convert the given text back to the flag.

3. I wrote this simple [script](./transformation.py) to decode the flag.

## Flag

picoCTF{16_bits_inst34d_of_8_b7f62ca5}

# Under the Rainbow (Forensics)

## Challenge

We have been searching far and wide, searching every stone (important or not), and we still haven't found this flag!

Do you see anything?

We are also given an image file `3_of_them.png`.

## Approach

1. Since this is a forensics challenge, the image itself doesn't reveal anything useful as expected. It is just an image of 3 cats.

2. Instead, I used `zsteg` and combined it with `grep` to retrieve the flag from the image file as follows:

<img src="./under_the_rainbow.png" width="75%">

## Flag

ggctf{s34rch_4_d4t4}

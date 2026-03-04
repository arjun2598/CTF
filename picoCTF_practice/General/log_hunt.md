# Log Hunt

## Challenge

We are given the file [server.log](./server.log), where we need to find the flag hidden within server logs.

## Approach

1. The first line in the file shows that each part of the flag is actually indicated with the string `FLAGPART`, so we just need to extract the parts of the file with this information.

2. We can use `grep FLAGPART server.log` to obtain only the lines containing the flag parts as output, but note that there is all the additional info from the logs per line, such as the timestamp.

3. Hence, we can go further and use `sed -n -e 's/.*FLAGPART: //p' server.log`, which only gives the part of each line after the matching expression `FLAGPART: `.

## Flag

picoCTF{us3_y0urlinux_sk1lls_cedfa5fb}

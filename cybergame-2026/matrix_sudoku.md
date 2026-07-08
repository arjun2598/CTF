# Matrix Sudoku (Reversing)

## Challenge

Can you solve this simple matrix? If your input satisfies the constraints, you will get decrypted flag.

We are given this file [get_flag.py](./get_flag.py).

## Approach

1. Reading through the code, we see that what is expected of us is to input the values 1 - 25 in order such that the constraints of each row are satisifed, as well as a diagonal constraint and a constraint of the sum of the first element of the first and last row of the matrix only.

2. If we use the input `1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25`, we can actually satisfy all constraints, solving the matrix and retrieving the flag.

## Flag

SK-CERT{simpl3_m47rix_sud0ku}

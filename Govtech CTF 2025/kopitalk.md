# Kopitalk

## Challenge

As Singapore approaches a super-aged society, healthier drink choices matter. But drinks at Singapore's coffeeshops (kopitiams) are sweetened by default.

So forget your Starbucks lingo - this Kopitiam Auntie only understands kopitiam lingo. Plus, auntie will reward you for healthier options - less sugar, less milk, you get the gistt.

What's more, Kopitiam Auntie recently modernized and now uses a website to receive pre-recorded voice orders. The website's voice recognition closely mimics auntie's favourite language

## Approach

1. Since the web page accepts audio files, use a text to speech converter to create an audio file with your order. I used the following: https://www.narakeet.com/app/text-to-audio/?projectId=699cebfc-e143-497d-a3c9-ceae9a36446c. There was a choice for Singaporean accent which suits `auntie's favourite language`

2. Since the challenge mentions rewarding for healthier options, I tried just using the keyword `kopi o kosong` as the lingo for ordering a coffee without sugar or milk. However, the page responds with `nowadays youngster never call auntie`

3. Therefore, include the word `auntie` before specifying the order, and the flag is obtained.

## Flag

AI2025{K0P1_P3NG_S1EW5IUS1U_DAI}
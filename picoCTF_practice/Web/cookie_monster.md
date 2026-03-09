# Cookie Monster Secret Recipe

## Challenge

Cookie Monster has hidden his top-secret cookie recipe somewhere on his website. As an aspiring cookie detective, your mission is to uncover this delectable secret. Can you outsmart Cookie Monster and find the hidden recipe?
You can access the Cookie Monster here and good luck

## Approach

1. The page is just a login page, and the source code doesn't reveal anything to us. Hence, just try logging in with random credentials.

2. From the challenge name and the hint given by the site as seen below, we know there is some information in the cookies.

<img src="./cookie_monster.png" width="75%">

3. The cookie **secret_recipe** has the following value: `cGljb0NURntjMDBrMWVfbTBuc3Rlcl9sMHZlc19jMDBraWVzXzQ3MzZGNkNCfQ%3D%3D`. Decoding this from base64 gives us the flag.

## Flag

picoCTF{c00k1e_m0nster_l0ves_c00kies_4736F6CB}

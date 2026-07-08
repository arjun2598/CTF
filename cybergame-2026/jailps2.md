# JailPS - safeps2

## Challenge

Get flag. Or git gud. Previous chall was too ez, right?

nc exp.cybergame.sk 7005

The [script](./jailps2.ps1) for this challenge is slightly modified from the previous challenge [JailPS1](./jailps1.md).

## Approach

1. The difference from the earlier challenge is that this time, no whitespaces are allowed, as well as the fact that `echo` will be prepended to the resulting payload.

2. Hence, the bypass is still similar, but we just need to make the echo execute anything before doing our exploit command.

3. After some researching and refining the payload, here is a working one: `echo 1;&("g"+"v")`

## Flag

SK-CERT{pow3R5H3LL_d03n7_C4r3_b0u7_5p4c3zzz}

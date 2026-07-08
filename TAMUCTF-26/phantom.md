# Phantom

## Challenge

The flag is somewhere around here or something idk

There is a link to the following repo: https://github.com/tamuctf/phantom#

Below is a snippet of the repo:

<img src="./phantom_repo.png" width="75%">

## Approach

1. Originally, there was no pull requests or issues as those were created by participants. So on first glance, the repo doesn't seem to give much clues on its own.

2. I tried cloning the repo locally and running some git commands such as `git log` to find some clues, but faced a dead end for most approaches.

3. Eventually, I found this writeup describing a similar challenge: https://blog.kulkan.com/our-github-forensics-ctf-challenge-for-ekoparty-0d26024b1dcb

4. From the writeup, there is a tool called `Gitxray` that analyses the repo for us. After installing it and running `gitxray -r https://github.com/tamuctf/phantom#`, there is a html file generated that gives all the info about the repo.

5. After scanning through the generated reports, the following comments section seemed like it might provide some clue to the flag:

<img src="./phantom_comments.png" width="75%">

6. After clicking on the older comments, we reach this page where the flag resides:

<img src="./phantom_flag.png" width="75%">

## Flag

gigem{917hu8_f02k5_423_v32y_1n7323571n9_1d60b3}

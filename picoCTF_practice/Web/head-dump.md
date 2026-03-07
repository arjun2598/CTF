# head-dump

## Challenge

Welcome to the challenge! In this challenge, you will explore a web application and find an endpoint that exposes a file containing a hidden flag.
The application is a simple blog website where you can read articles about various topics, including an article about API Documentation. Your goal is to explore the application and find the endpoint that generates files holding the server’s memory, where a secret flag is hidden.
The website is running picoCTF News.

## Approach

1. After looking around the webpage and inspecting element as the first step, I searched for `/api` to see if there was a hidden api route as hinted by the challenge description. Turns out that there was one in this div as follows:

```
<div class="mb-4">
  <p class="text-gray-800">Explore backend development with us <a href="" class="text-blue-600">#nodejs</a> ,
    <a href="" class="text-blue-600">#swagger UI</a> , <a href="/api-docs" class="text-blue-600 hover:underline">#API Documentation</a>
  </p>
</div>
```

<img src="./head-dump.png" width="75%">

2. Now, after accessing the API docs, we discover that there is a `/heapdump` endpoint that returns information about the memory of the website. Accessing this endpoint downloads the file `heapdump-1772926023082.heapsnapshot`.

3. If we try to just `cat` the file, there is a lot of irrelevant information that makes it harder to find the flag. Instead, use `grep "picoCTF{"` to retrieve the flag directly.

## Flag
picoCTF{Pat!3nt_15_Th3_K3y_dc0756a3}
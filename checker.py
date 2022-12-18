import requests

BOTS = ["http://192.168.1.35:4200","https://lol.lol/"] # EXAMPLE bots
WORKING_BOTS = []
for i in range(len(BOTS)):
 r=requests.get(BOTS[i])
 if r == "pong":
    print(f"{i} bot(s) online... [{BOTS[i]}]"  + WORKING_BOTS.extend[BOTS[i]])
    if i > len(BOTS):
        input('done')
        input()
        input()
        input()
        input()
        break

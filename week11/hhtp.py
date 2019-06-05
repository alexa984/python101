import requests
import numpy as np
import matplotlib.pyplot as plt
#curl register.start.bg/ | egrep "<a href=.*.bg</a>" >urls.txt
#cat urls.txt | sed -E "s|<a.*>(.*.bg)</a>|\1|g" > hrefs

with open('hrefs.txt', 'r') as f:
    content = f.readlines()
content = [line.strip('\n') for line in content]

servers = dict()

for line in content:
    try:
        url = 'http://' + line
        response = requests.get(url)
        server = response.headers['Server']
        server = server.split('/')[0]
        if server in servers:
            servers[server]+= 1
        else:
            servers[server] = 1 
    
    except:
        continue


plt.bar(servers.keys(), servers.values(), 0.5, color='g')
plt.show()
# print(servers)
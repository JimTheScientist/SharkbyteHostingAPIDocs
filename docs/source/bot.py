import wispyjim

API_KEY = "YOUR_API_KEY_HERE"

ptclient = wispyjim.Wispy(api_key=API_KEY, url='https://sharkbytepanel.panel.gg/')

servers = ptclient.get_all_servers()
print(servers)
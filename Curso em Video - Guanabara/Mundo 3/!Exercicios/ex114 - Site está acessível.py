# import requests
# try:
#     site = requests.get('http://www.pudim.com.br/')
# except:
#     print('Site inacessivel!')
# else:
#     print('Site está online!')
    
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br/')
except:
    print('Site inacessivel!')
else:
    print('Site está online!')
    #print(site.read()) # Pega o codigo do site
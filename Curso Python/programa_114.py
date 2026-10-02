import urllib
import urllib.request

try:
    site = urllib.request.urlopen("http://www.google.com") # tentar abrir site
except urllib.error.URLError:
    print("deu erro")
else:
    print("todo ok")
    print(site.read()) # ler codigo site
import urllib.request as url

url.urlretrieve("https://www.google.com/","webpage.html")

for line in open("webpage.html"):
    print(line.strip())
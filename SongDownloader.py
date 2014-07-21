import re
import urllib
import urllib2

print "Enter your The Song You want to download"
user_input=str(raw_input())
user_input=user_input.replace(" ","_")

url="http://mp3skull.com/mp3/"+user_input+".html"
html_doc=urllib.urlopen(url)
html=html_doc.read()
regex='<a href="(.+?).mp3"'


slist=re.compile(regex)

songlist=re.findall(slist,html)

print "Downloading"

#to download the mp3
urllib.urlretrieve(songlist[0]+".mp3",user_input+".mp3")
print "Done"
print "Saved as -" + user_input + ".mp3"	
 

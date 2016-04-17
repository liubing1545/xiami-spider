import requests
from os.path import dirname, abspath
from extract import extract, extract_all
import re
from str2url import str2url
import os
#RE_CN = re.compile(ur'[\u4e00-\u9fa5]+')

print "album url:"
albumurl = raw_input(">")
print "store in:"
storeinpc = raw_input(">")
if os.path.exists(storeinpc) is False:
    print "wrong path!"
    exit()

PREFIX = dirname(abspath(__file__))

    #albumurl = "http://www.xiami.com/album/307474"
headers = {'User-Agent': 'Mozilla/5.0'}
r = requests.get(albumurl,headers = headers)

#write in file
#target.truncate()
#target.write(r.content)
#target.close()

if r.status_code == 200:
    for songid in extract_all('<a href="/song/', '"', r.content):
        songurl = "http://www.xiami.com/song/playlist/id/"\
        "%s/object_name/default/object_id/0"%songid
        r2 = requests.get(songurl,headers = headers)

        user_agent = "\"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:16.0)"\
        " Gecko/20100101 Firefox/16.0\""
        
        #print r.content
        if r2.status_code == 200:
            for path, name in zip(
                extract_all('<location>', '</location>', r2.content),
                extract_all('<title><![CDATA[', ']]></title>', r2.content)
            ):
                path2 = str2url(path)
                if (path2.find('%') != -1):
                    path2 = path2.replace('%','%%')

                convdecode = name.decode('utf-8',"ignore").encode("gb18030","ignore")

                print "downing the song: %s" %convdecode
                
                r3 = requests.get(path2,headers = headers)
                with open("%s/%s.mp3"%(storeinpc,convdecode),"wb") as down:
                    down.write(r3.content)

                print "***********************"
                    
            #break
        else:
            print r2.status_code
else:
    print r.status_code
        
            
        
    

                    
                    

import requests
import random
import re
import subprocess

file_path = "C:/Users/_______/Desktop/Tor Browser/Browser/TorBrowser/Tor/tor.exe"

def ahmia_scraper(query, days):

    subprocess.call([file_path])

    session = requests.session()
    session.proxies = {'http':  'socks5h://127.0.0.1:9050',
                       'https': 'socks5h://127.0.0.1:9050'}

    if " " in query:
        query = query.replace(" ", "+")

    url = "http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion/search/?q={}&d={}".format(query, days) #The onion link for ahmia at the time
    #Random fake user agents
    ua_list = [ "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A", #Safari
                "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:77.0) Gecko/20100101 Firefox/77.0", #Firefox
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36", #Chrome
                "Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16.2", #Opera
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"] #Edge
   
    content = session.get(url).text
    
    regexquery = "\w+\.onion" #finding onion links
    links = re.findall(regexquery, content)
    links = [i for n, i in enumerate(links) if i not in links[:n]]
    links.remove('zerdg.onion')

    print(links)

    for i in links:
        url = "http://"+i+"/"
        try:
            print("Accessing " +i+" ...")
            result = session.get(url).text
            file = open(i+".html", "w+")
            file.write(result)
            file.close()
        except:
            break

ahmia_scraper("thank you for checking out this project", 1)
import requests
import random
import re
import subprocess

file_path = "C:/Users/______/Desktop/Tor Browser/Browser/TorBrowser/Tor/tor.exe"

def ahmia_scraper(query, days):

    if " " in query:
        query = query.replace(" ", "+")

    url = "https://ahmia.fi/search/?q={}&d={}".format(query, days)
    #Random fake user agents
    ua_list = [ "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A", #Safari
                "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:77.0) Gecko/20100101 Firefox/77.0", #Firefox
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36", #Chrome
                "Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16.2", #Opera
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"] #Edge

    ua = random.choice(ua_list)
    headers = {'User-Agent': ua}
    request = requests.get(url, headers=headers)
    content = request.text

    if request.status_code == 200:
        print("Request went through. \n")
    
    regexquery = "\w+\.onion" #finding onion links
    mined_data = re.findall(regexquery, content)
    mined_data = [i for n, i in enumerate(mined_data) if i not in mined_data[:n]]
    mined_data.remove('zerdg.onion')

    subprocess.call([file_path])

    session = requests.session()
    session.proxies = {'http':  'socks5h://127.0.0.1:9050',
                       'https': 'socks5h://127.0.0.1:9050'}
    
    print(mined_data)

    for i in mined_data:
        url = "http://"+i+"/"
        try:
            print("Accessing " +i+" ...")
            result = session.get(url).text
            file = open(i+".html", "w+")
            file.write(result)
            file.close()
        except:
            pass

ahmia_scraper("leaked password database", 1)
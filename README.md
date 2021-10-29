# Deep Web Scraper

I am going to assume that you have Tor installed already and you know where it is. Also, you should have a VPN before you enter the deep web.

This script will perform the following steps:

1. Using the given deep web search engine site, input keyword to search for onion links
  -- Use deep_scraper.py if your search engine can be found on clear web
  -- Use deep_scraper_onion.py if your search engine is an onion link itself

2. Use Regex to extract all .onion links and put them in a list

3. Go through each link in the list and save them as html offline

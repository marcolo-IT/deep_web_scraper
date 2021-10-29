# Deep Web Scraper

I am going to assume that you have Tor installed already and you know where it is. Also, you should have a VPN before you enter the deep web.

By default, I am using ahmia as the search engine. Just need to change the first "url" variable if you wish to use a different search engine.

This script will perform the following steps:

1. Using the given deep web search engine site, input keyword and time period to search for onion links
  >> Use deep_scraper.py if your search engine can be found on clear web. Otherwise, use deep_scraper_onion.py 

2. Use Regex to extract all .onion links and put them in a list

3. Go through each link in the list and save them as html offline

# Threat hunt strategy

- Enter attack terms along with your organization name or a term that you know only your organization uses
- Target forums
- Ask for sample data to verify its validity
- Blend into the community

import time
import re
import json
import urllib
import pyfiglet
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen

ascii_banner = pyfiglet.figlet_format("SOCIJACK")
print(ascii_banner)
print("Loading, it may take a moment (depending on the size of your accounts.txt) \n")

with open('accounts.txt') as f:
    accounts_username = f.readlines()
accounts_username = [x.strip() for x in accounts_username]

# Main variable
correct_names = []

for username in accounts_username:
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    browser = webdriver.Chrome('./chromedriver', options=chrome_options)
    browser.get('https://www.instagram.com/' + username + '/?hl=en')
    Pagelength = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    description = ""
    links = []
    source = browser.page_source
    data = bs(source, 'html.parser')
    main = data.find("main")
    posts = main.find("div")

    last_div = None
    for last_div in posts:pass
    if last_div:
        content = last_div.getText()

    links_from_posts = last_div.findAll('a')
    all_links = []
    for link in links_from_posts:
        if re.match("/p", link.get('href')):
            all_links.append('https://www.instagram.com' + link.get('href'))



    all_usernames = []
    for i in range(len(all_links)):
        try:
            page = urlopen(all_links[i]).read()
            data = bs(page, 'html.parser')
            body = data.find('body')
            script = body.find('script')
            raw = script.contents[0].replace('window._sharedData =', '').replace(';', '')
            json_data = json.loads(raw)

            posts = json_data['entry_data']['PostPage'][0]['graphql']
            # all text description
            description = posts['shortcode_media']['edge_media_to_caption']['edges'][0]['node']['text']
            # all usernames in text description
            results = re.findall("\@[^\s]+", description)
            for u in results:
                all_usernames.append(u)
        except:
            np.nan

    # Clean usernames
    sponge = []
    for i in all_usernames:
        # Strip dots
        x = i.replace('.', '')
        # Strip !
        x = x.replace('!', '')
        # Strip ?
        x = x.replace('?', '')
        # Strip ?
        x = x.replace('#', '')
        # Strip @
        y = x.replace('@', '')
        # Lower case all
        z = y.lower()
        sponge.append(z)

    correct_names = list(dict.fromkeys(sponge))

## Try if a user exists or not
for user in correct_names:
    try:
        response = urlopen("https://www.instagram.com/" + user)
    except urllib.error.HTTPError:
        print("[FOUND]=> " + str(user) + " is available !")
        # Webhooks contact
        ## response = urlopen("http://x.x.x.x:3000/ig-" + user)

print("[INFO] => Done.")

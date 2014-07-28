#!/usr/bin/python
import shutil
import requests
import json
import re
import argparse

# download html page of given dropbox url
parser = argparse.ArgumentParser(description='Download a Dropbox folder')
parser.add_argument('url', help='dropbox folder url')
url = parser.parse_args().url
dropboxpage = requests.get(url).content

# search for files in the page javascript
regex = re.compile("init_folder(.*)")
r = regex.search(dropboxpage)
matches = r.groups()

regex_imagedata = re.compile("\[{(.*)")
raw_imagedata = regex_imagedata.search(matches[0]).group()
raw_imagedata = raw_imagedata.rstrip(')')
imagedata = json.loads(raw_imagedata)

# download and store files
for obj in imagedata:
    print("downloading %s" % obj['filename'])
    response = requests.get(obj['dl_url'], stream=True)
    with open(obj['filename'], 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response

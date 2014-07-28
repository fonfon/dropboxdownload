## Download a Dropbox folder
Quick and dirty download all files of a dropbox folder. This script does not
take care of subfolders, malevolent filenames or any existing files. I use it
to download large public dropbox folders (that dropbox refuses to zip) without
a dropbox account.

## Installation (for Linux)
```
git clone git@github.com:fonfon/dropboxdownload.git
cd dropboxdownload
pip install -r requirements.txt
sudo cp dropboxdownload.py /usr/local/bin/
sudo chmod a+x /usr/local/bin/dropboxdownload.py
```

## Usage
```
dropboxdownload.py https://www.dropbox.com/sh/xxxx/yyyy/yourFolder
```

## Download the content of Dropbox folders into the current directory
Quick and dirty download files of a dropbox folder into your current filesystem
older. This script does not take care of subfolders, malevolent filenames or
any existing files. It can be handy to download a large public dropbox folder
without a dropbox account.

## Installation (for Linux)
git clone git@github.com:fonfon/dropboxdownload.git
cd dropboxdownload
pip install -r requirements.txt
sudo cp dropboxdownload.py /usr/local/bin/
sudo chmod ugo+x /usr/local/bin/dropboxdownload.py

## Usage
dropboxdownload.py https://www.dropbox.com/sh/xxxx/yyyy/yourFolder

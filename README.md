blacklist
=========

A simple python script to blacklist some internet sites on a pc.

USAGE:
make it executable with `chmod u+x blacklist.py`, then 
* `sudo ./blacklist.py act` for activating the blacklist
* `sudo ./blacklist.py deact` for deactivating



It works by redirecting sites contained in /etc/hosts to 127.0.0.1. As a consequence the script must be executed with **sudo** permission.

Sites must be specified in the `SITES_TO_IGNORE` dictionary, in the script.

`search_item` key must be a string contained in the address. It needs for removing purpose.

It's **STRONGLY** recommended that you save a copy of `hosts` file. Please DO NOT name this backup as `hosts.bak`

_Tested on linux Ubuntu 12.04LTS, python 2.7.3_

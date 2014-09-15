blacklist
=========

A simple python script to blacklist some internet sites on a pc.
One of the following command lines arguments must be passed: 
* `act` for activating the blacklist
* `deact` for deactivating

Tested only on linux Ubuntu 12.04LTS. It works by redirecting sites contained in /etc/hosts to 127.0.0.1

Sites must be specified in the dictionary.

`search_item` key must be a string contained in the address. It needs for removing purpose.

It's **STRONGLY** recommended that you save a copy of `hosts` file. Please DO NOT name this backup as `hosts.bak`

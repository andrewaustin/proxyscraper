proxyscraper
============

Scrapes ip addresses from a webpage of the form w.x.y.z:port Once it has a list
is tries to connect to each proxy to see if they are valid. If they are valid it
writes the valid proxy to proxies.txt.

Usage
-----
Edit the *url* variable in proxy.py to point to your source of proxies to scrape. Then
run: python proxy.py

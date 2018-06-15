# squid-python-redirect

# How it works

urls.json contains key-value pairs of redirected sites.

redirect.py get in one requested URL from squid. Then it checks if the requested URL is in the file urls.json, it sends the response to the server with the  changed address.

Please, add these string to your squid config file:

```
url_rewrite_children
url_rewrite_program path_to_redirect.py path_to_urls.json
```
path_to_resirect.py - this directory where redirect.py is
redirect.py get 1 argument with directory where urls.json is

Also remember about 
1. ol changing the rights to run these files.
2. ol specify path to python interpreter in redirect.py

vidal-api.py
============
## Build status

[![Build Status](https://travis-ci.org/softwarevidal/vidal-api.py.svg)](https://travis-ci.org/softwarevidal/vidal-api.py)

How to install
--------------

```
pip install vidal-api.py
```

Using the API
------------

Just create client with your VIDAL Credentials : 

```
>>> from vidal.client import VidalClient
>>> client = VidalClient(api_key = "my_api_key")
```

And you can use any kind of API chaining your commands *lazyli* and then call an http verb method like **get()** to trigger the API call.

Example : 
```
# this will call "http://api.vidal.fr/rest/api/product/94930/packages" with a GET verb.
>>> client.product(94930).packages.get()

# search example :
>>> client.products.get(q = "amox")

# or any kind of get parameters :
>>> client.product(94930).packages.get(aggregates = "product")
```

Setting up dev environment
--------------------------
You need Python installed and pip, then just run :

```pip install -r requirements.txt```

and to execute the tests : 

```
nosetests
```

Source code convention
----------------------

Default indendation is **4 spaces** no tabs.

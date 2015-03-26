### DCP-Stream

Allows you to listen to Couchbase DCP stream. DCP(Database change protocol) is a new protocol that Couchbase v3.0 and later support.

Sample run:

* Run `cbworkloadgen` in a loop(you could use any load-gen, sample program written on top of Couchbase SDK or use open-source memcached clients)

```
/opt/couchbase/bin/cbworkloadgen -i 100 -j -l
.....................................................
.....................................................
.....................................................
```

* Run `dcpstream.py` from the repository and you will all mutations showing up in stdout

```
$ python dcpstream.py
{“name”: “pymc0”, “age”: 0, “index”: 0, “body”: “0000000000”}
{“name”: “pymc1”, “age”: 1, “index”: 1, “body”: “0000000000”}
{“name”: “pymc7”, “age”: 7, “index”: 7, “body”: “0000000000”}
{“name”: “pymc5”, “age”: 5, “index”: 5, “body”: “0000000000”}
{“name”: “pymc6”, “age”: 6, “index”: 6, “body”: “0000000000”}
{“name”: “pymc8”, “age”: 8, “index”: 8, “body”: “0000000000”}
{“name”: “pymc3”, “age”: 3, “index”: 3, “body”: “0000000000”}
..
..
```

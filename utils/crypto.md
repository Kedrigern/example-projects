Cryptography
============

List of ciphers:
```
openssl list-cipher-commands
```

Encrypt:
```
openssl aes-256-cbc -in <input> -out <output>
```

Decrypt:
```
openssl aes-256-cbc -d -in <input> -out <output>
```

Steganography
-------------
Encrypt:
```
steghide embed  --embedfile tajna.zprava.txt --coverfile obrazek.jpg  --stegofile obrazek.plus.jpg
```

Decrypt:
```
steghide extract --stegofile obrazek.plus.jpg --extractfile tajna.zprava.txt
```

Links
-----

* [Komunikujeme a ukládáme data bezpečně s PGP/GPG](http://www.linuxexpres.cz/software/komunikujeme-a-ukladame-data-bezpecne-s-pgp-gpg-1-uvod)
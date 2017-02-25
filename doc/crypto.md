# Cryptography


## OpenSSL 

List of ciphers:

```
openssl list-cipher-commands
```

### Encrypt:

```
openssl aes-256-cbc -in <input> -out <output>
```

### Decrypt:
```
openssl aes-256-cbc -d -in <input> -out <output>
```

### Sign

#### JSignPdf

[Github](https://github.com/kwart/jsignpdf), [download](http://sourceforge.net/projects/jsignpdf/files/latest/download?source=files)

Gui: `java -jar /opt/jsignpdf/JSignPdf.jar`

Cli: `java -jar /opt/jsignpdf/JSignPdf.jar -kst PKCS12 -ksf <key>.pfx -ksp <key_password> -V <file>.pdf`

### Convert PFX to PEM

Convert `certificate.pfx` into `certificate.cer` (or `certificate.pem`):

```
openssl pkcs12 -in certificate.pfx -out certificate.cer [-nodes]
```

With nodes: New key is not encrypted.

NOTE: While converting PFX to PEM format, openssl will put all the Certificates and Private Key into a single file. You will need to open the file in Text editor and copy each Certificate & Private key(including the BEGIN/END statements) to its own individual text file and save them as certificate.cer, CAcert.cer, privateKey.key respectively.

## Steganography
-------------
### Encrypt:

```
steghide embed  --embedfile tajna.zprava.txt --coverfile obrazek.jpg  --stegofile obrazek.plus.jpg
```

### Decrypt:

```
steghide extract --stegofile obrazek.plus.jpg --extractfile tajna.zprava.txt
```




Links
-----

* [Komunikujeme a ukládáme data bezpečně s PGP/GPG](http://www.linuxexpres.cz/software/komunikujeme-a-ukladame-data-bezpecne-s-pgp-gpg-1-uvod)
* [](https://paulbradley.org/digitally-sign-pdf-files/)
* [PortableSigner](https://github.com/pflaeging/PortableSigner2)
* [jSignPdf](https://github.com/kwart/jsignpdf)


# Ldap

Jedná se sice o prastarý a nepřiliš přívětivý protokol, avšak nejvíce rozšířenou autentifikační vrstvu.

LDAP je *lightweight protocol for accessing directory servers*. *Directory server* je *hierarchical object orientated database*. 

V praxi to znamená, že správce si určuje komplexní DB schéma víceméně pomocí **objektů**. Lightweight protože je jednoduší než X.500 protokol. Je optimalizovaný pro čtení (proto strom). Je case insensitive.

Objekty v LDAPu obsahují **atributy**. Ty jsou množiny párů klíč-hodnota. Protože jsou data v rámci LDAP strukturovaná, tak objekty mohou obsahovat pouze validní klíče. Validita je zavislá na typu objektu (na schématu). Třídy mohou mít atributy povinné (mandatory) a volitelné (optional). Atribut může být single nebo multi. Multi dovoluje více hodnot (např. více emailových adres u jedné osoby). Atributy mohou mít aliasy nebo zkratky (cn je zkratka pro CommonName).

Matoucí je, že objekty mohou být více jak jednou třídou. Třídy:

- **strukturální** (structural): každý objekt má právě jednu. Jsou určeny k mapování fyzického obejktu, např. osoby či sítě. Tato třída nemůže být u obejtku změněna.
- **pomocné třídy** (auxilary): určují další typy atributů. Mohou být měněny u již existujícícho objektu.
- **abstraktní třídy** (abstract): nepřiřazují se přímo k obejtku, ale využívají je ostatní třídy v rámci hiearchie.

## Slovník

| Zkratka | Význam             | Příklad                                     | Vysvětlení                                               |
|---------|--------------------|---------------------------------------------|----------------------------------------------------------|
| DN      | Distinguished Name | DC=cz,DC=pirati,OU=people,cn=ondrej.profant | jednoznačné určení v rámci stormu (hiearchie)            |
| DC      | Domain component   | google; com; cz; pirati                     | lze používat i geografické specifikace, ale DNS je lepší |
| OU      | Organization unit  | people; groups                              |  |
| CN      | Common name        |                                             |  |
| OID     | Object ID          | 1.3.6.1.4.1.1466.115.121.1.15{16}           | 16-character sized Unicode string |
| UID     | Unique ID          | ISBN; ID; URI                               | jednoznačný identifikator |
| DIT     | Directory Information tree | | |
| LDAP    | Lightweight directory protocol | | |
| LDIF    | LDAP Data interchange files | | |

## Fedora 24

### Install

```bash
dnf -y install openldap-servers openldap-clients
cp /usr/share/openldap-servers/DB_CONFIG.example /var/lib/ldap/DB_CONFIG
chown ldap. /var/lib/ldap/DB_CONFIG
systemctl start slapd
systemctl enable slapd 
```

### Configure

```bash
# generate encrypted password into cli
slappasswd
```

### Grafická správa

- [Luma][http://luma.sourceforge.net] LDAP browser napsaný v Pythonu (PyQt).
- [Apache directory studio][] robustní řešení postavené nad Eclipse

## Schéma

```
                       DC = CZ
                          |
                      DC = Pirati
       	__________________|_______________________	
       /                  |                       \
OU = Users          OU = Systems             OU = organization
|-CN=John Doe      /      |    \                      |      
|-...       CN=Redmine CN=Forum CN=Wiki            OU = CF  
                                     _________________|______________
                                    /             |           |      \
                                OU=Praha   OU=Jihomoravsky  OU=Zlin   ...
```

[ldap-basics]: http://www.davidpashley.com/articles/ldap-basics/
[ldap-a-gentle-introduction]: https://hynek.me/articles/ldap-a-gentle-introduction/
[what-are-cn-ou-dc-in-an-ldap-search]: http://stackoverflow.com/questions/18756688/what-are-cn-ou-dc-in-an-ldap-search
[ldap]: http://www.zytrax.com/books/ldap/ch2/
[fedora23]: https://www.server-world.info/en/note?os=Fedora_23&p=openldap
[Luma]: http://luma.sourceforge.net
[Apache directory studio]: http://directory.apache.org/studio/

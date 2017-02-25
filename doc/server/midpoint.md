# midPoint

## Instalace

Nejjednoduší je nainstalovat [tomcat](tomcat.md) a použít distribuční war soubor.

```bash
yum install tomcat tomcat-webapps tomcat-admin-webapps
service tomcat start
service tomcat status
```

Zda tomcat chodí zjistíme na adrese: `http://127.0.0.1:8080/`.

Konfigurační soubor: `/etc/tomcat/tomcat.conf`

My potřebujeme nastavit uživatele, ty nastavíme v:
`/etc/tomcat/tomcat-users.xml`

Kde doplníme něco jako:

```xml
<role rolename="admin-gui"/>
<role rolename="manager-gui"/>
<user username="tomcat" password="s3cret" roles="admin-gui,manager-gui"/>
```

Zkopírujeme MidPoint do tomacatu: 
`cp midpoint.war /var/lib/tomcat/webapps/`
a na stránce `http://127.0.0.1:8080/manager/` spustíme (`run`).

## Konfigurace MidPoint

Default user: `administrator`, heslo: `5ecr3t`

Terminilogie:



         | Znamená             | Uložen v            | Příklad  |
---------|---------------------|---------------------|----------|
User     | Fyzická osoba       | midPoint repository | John Doe |
Account  | Záznam použitý k přístupu do systému | a Resource | jsmith123 uid=doejr,ou=people,dc=example,dc=com |
Resource | Externí systém, který midPoint řídí | N/A | LDAP server ds1.example.com |



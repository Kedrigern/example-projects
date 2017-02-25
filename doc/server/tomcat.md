# Tomcat

Tomcat je webový/aplikační server čistě v Java.
Má jednoduché webové rozhraní a možnost distribuce aplikací pomocí balíčků (`*.war`).

## Instalace Tomcat

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

Zkopírujeme aplikaci do tomacatu: 
`cp app.war /var/lib/tomcat/webapps/`
a na stránce `http://127.0.0.1:8080/manager/` spustíme (`run`).


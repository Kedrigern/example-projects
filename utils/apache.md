

#Apache

## Autorizace
Autorizace: http://radio.feld.cvut.cz/local/web-info/autorizace.html

## Rest
http://httpd.apache.org/docs/2.2/mod/mod_dav.html

##VirtualHosts

Nejdříve si přesměrujeme v `etc/hosts` domény:
```
127.0.0.1		localhost.localdomain localhost
127.0.0.1		<domena>.lo
```

Poté vysvětlíme Apachi, co má s kterou doménou dělat:
```
# Standard behaviour
<VirtualHost *:80>
DocumentRoot /var/www/html
ServerName localhost
</VirtualHost>

# Our local domain
<VirtualHost *:80>
DocumentRoot /var/www/html/<project>/<document_root>
ServerName <domena>.lo
```

#Systems
##Ubuntu
Config: `/etc/apache2/apache2.conf`

Restart: `sudo service apache2 restart`

### Links
* http://maketecheasier.com/install-and-configure-apache-in-ubuntu/2011/03/09
* http://stackoverflow.com/questions/2934554/how-to-enable-and-use-http-put-and-delete-with-apache2-and-php
* https://www.digitalocean.com/community/articles/how-to-set-up-apache-virtual-hosts-on-ubuntu-12-04-lts

##Fedora
Daemon name is `httpd` and run under user/group `apache`

Config `/etc/httpd/conf/httpd.conf`

Restart: `sudo service httpd restart`

### Links
* http://www.thegeekstuff.com/2011/07/apache-virtual-host/
* http://diskuse.jakpsatweb.cz/?action=vthread&forum=31&topic=9828
* http://httpd.apache.org/docs/2.2/vhosts/examples.html
* http://blog.webkitchen.cz/virtualhosty
* https://library.linode.com/web-servers/apache/installation/fedora-14

##OS X
Apache je předinstalován, ale není zapnut

`etc` je v `private/etc`

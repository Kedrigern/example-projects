#/usr/bin/env bash
# http://www.openldap.org/faq/data/cache/104.html
# testet on Fedora 24

echo "Stopping LDAP and trashing database ..."

sudo systemctl stop slapd
sudo rm -f /var/lib/ldap/*


echo "Rebuilding database ..."

echo "Starting LDAP ..."

sudo systemctl start slapd

sleep 5

echo "Querying database ..."

ldapsearch -b 'dc=pirati,dc=cz' 'objectClass=*'

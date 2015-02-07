# Localhost

Pár rad k localhostu. 

Pokud používáte nějakou složitější konfiguraci (více jazyků, nástrojů etc.), tak zvažte využití [dockeru](docker.md). Krom toho, že pomůže vám, pomůže i komukoliv dalšímu, kdo by se chtěl připojit (pomoci vám).

## Co zkontrolovat

1. zapnutí server démona
1. zapnutí db démona
1. firewall
1. máte nainstalované a zkompilované všechny komponenty projektu (`composer install`, `bower install`)
1. jsou připravené všechny konfigy (např. example změněn na ostrý, vyplněna DB)
1. přístupová práva (`/etc/httpd/logs`)
1. selinux (log: `/var/logs/messages`, více o [selinux](permissions/selinux.md))

PS: Používám Fedoru, např. na debianu bude namísto `httpd` `apache`.
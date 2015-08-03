# CoreOS
Minimalistický systém pro hostování [dockeru](docker.md).

## Cloud-config

Použije se při bootu.

Na prvním řádku musí být `#cloud-config`. Nejvyšší direktivy jsou: `coreos`, `ssh_authorized_keys`, `hostname`, `users`, `write_files`, `manage_etc_hosts`

### ssh_authorized_keys

Přidá uživateli `core` daný klíč.

* [](http://www.linuxexpres.cz/software/coreos-proc-byste-o-nem-meli-uvazovat)
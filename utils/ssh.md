## Zkratky

V souboru `~/.ssh/config` mají formát:

```
Host ex

HostName example.com
User user
Port 123
ServerAliveInterval 30
ServerAliveCountMax 120
```

Následně se parametr `Host` používá kdekoliv bychom měli zadávat plnou adresu. Např. namísto: `ssh user@examplex.com:123` zadáme jen `ssh ex`.

## Klíče

V SSH se využívá asymetrická kryptografie. Máme veřejný a privátní klíč (a jejich otisky). Privátní je potřeba opravdu udržet privátní (a je dobré u něj mít pasphrase). Veřejný lze naopak vystavit ven.

### Generování páru klíčů

Klíč se vším všudy vygenerujeme tímto příkazem:
`ssh-keygen -C 'some comment' -b 2048  -t rsa -f filename`
Budeme ještě dotázani na passphare, důrazně ji doporučuji vyplnit. Také je dobré rozumně popsat komentář.


## Přihlašování na server pomocí klíče

Na serveru vložíme do `~/.ssh/authorized_keys` náš veřejný klíč. Např. tímto příkazem:
```bash
ssh USER@HOST "mkdir -p ~/.ssh"
cat ~/.ssh/id_rsa.pub | ssh USER@HOST "cat >> ~/.ssh/authorized_keys"
```
### Známé servery

Pokud se připojujeme k serveru poprvé, tak se nás SSH zeptá, zda odpovídá fingerprint, což v budoucnu může zabránit MIM útoku. Známe servery vy

### Testování

Github:
```
ssh -T git@github.com                             
```

### Debuging

```
SElinux: restorecon -r /home/user/.ssh
```

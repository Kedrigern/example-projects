# Shell

#Bash

### Vyznaceni vetve z gitu

Ubuntu:
 1. Potrebujeme tento skript: `https://github.com/git/git/blob/master/contrib/completion/git-prompt.sh`
 1. Ten vlozime do `.bashrc` pomoci `source path-to-scipt`
 1. Nasledne nastavime promennou `PS1="\e[1;33m\u\e[0;37m:\w\$(__git_ps1)\$ "`

Fedora: [wiki](https://fedoraproject.org/wiki/Git_quick_reference)

Promenne:
`PS1='\e[1;33m\u\e[0;37m:\W$(declare -F __git_ps1 &>/dev/null && __git_ps1 " (\e[1;32m%s\e[0;37m)")\$ '`


### Konkretni utilitky
Nalezení otevřených ssh v síti:
```nmap -p 22 --open -sV 10.0.0.0/24```

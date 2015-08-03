
# Python

Výborná kniha pro seznámení s Pythonem je [Ponořme se do Python(u)](http://knihy.nic.cz/). 

## modules

## Virtual enviroment

Jsou izolovaná prostředí pro Python. 

## pip

Pip je distribuční systém pro python. Má stadardní ovládání:

```bash
pip search wget
sudo pip install wget
sudo pip uninstall wget
```

Nainstalování libovolného (kompatibilního) repozitáře:

```bash
pip install git+http://github.com/kedrigern/pyexample
pip install <local/path>
```

I takovéto repozitáře jdou přes pip odinstalovat.

Pip umí fixovat verze a instalovat update:

```bash
pip install --upgrade <package>
```

# Tetra

Tetra je radiová síť. Mimojiné využíváná HMP pro potřeby MP, DPP...

1. Nainstalujeme závislosti:
	- `sudo dnf install libosmocore gnuradio gr-osmosdr python3 python2`

2. Nainstalujeme [tetra-listener][]:
	- `git clone https://github.com/itds-consulting/tetra-listener.git`
	- `cd tetra-listener`
	- `git submodule init`
	- `git submodule update`
	- `./build.sh`

3. Nainstalujeme [tetra-multiframe-sds][]:
	- `git clone https://github.com/itds-consulting/tetra-multiframe-sds.git`
	- `cd tetra-multiframe-sds`
	- `cp tetra-listener.patch ../tetra-listener/`
	- `cp osmo-tetra.patch ../tetra-listener/osmo-tetra/`
	- `cd ../tetra-listener`
	- `git apply tetra-listener.patch`
	- `cd osmo-tetra/ && git apply osmo-tetra.patch && cd ..`
	- `./build.sh`

4. Konfigurace
	- `cd tetra-listener/radio-tetra`
	- `cp config.sh config.sh.bak`
	- zeditujeme `config.sh`

5. Provoz v terminálech spustíme:
	- `tshark -i lo`
	- `tetra-listener/radio-tetra/tetra.sh`
	- `tetra-multiframe-sds/sds-parser.py -p /tmp/fifos`
	- `tetra-listener/radio-tetra/tetra-inotify.sh`

6. Data jsou ukládána:
	- `~/tetra-rec` (formát ogg)
	- `tetra-multiframe-sds/sds.db`, čili s tím můžeme pracovat v [sqlite][../db/sqlite.md]: `sqlite3 sds.db 'select * from sds'`


[tetra-listener]: https://github.com/itds-consulting/tetra-listener
[tetra-multiframe-sds]: https://github.com/itds-consulting/tetra-multiframe-sds

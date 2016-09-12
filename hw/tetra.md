
# Tetra

Tetra je radiová síť. Mimojiné využíváná HMP pro potřeby MP, DPP...

## HW

K jejímu poslechu potřebujeme RTL-SDR, tedy nějaký DVBT+FM usb dongle. Stojí 250-400 Kč. My samozřejmě nepotřebujeme dalkové ovládání. Já osobně používám Realtek [RTL2832U][].

## Návod

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
	- zeditujeme `config.sh`:
		- `STREAMS` počet streamů, doporučuji 25-30
		- `TUNE_FREQ=424400e3` dle měření antény
		- `TUNE_PPM=36` dle měření antény
	- občas je třeba změnit `tetra-multiframe-sds/config.py`, kde jsou 2 verze tshark příkazu

5. Provoz v terminálech spustíme:
	- `tshark -i lo`
	- `tetra-listener/radio-tetra/tetra.sh`
	- `tetra-multiframe-sds/sds-parser.py -p /tmp/fifos`
	- `tetra-listener/radio-tetra/tetra-inotify.sh`

6. Data jsou ukládána:
	- `~/tetra-rec` (formát ogg)
	- `tetra-multiframe-sds/sds.db`
		- schéma tabulky zobrazíme: `sqlite3 sds.db .schema`
		- čili s tím můžeme pracovat v [sqlite][]: `sqlite3 sds.db 'select * from sds;`
		- zajímavý je též sloupec `DS_T4_TRANSFER_USER_DATA_ASCII_INDEX `, který udává míru textu v SDS

[sqlite]: ../db/sqlite.md
[RTL2832U]: https://www.google.cz/search?q=Realtek+RTL2832U&ie=utf-8&oe=utf-8&gws_rd=cr&ei=t8jWV6ewOoKnad24uKAK#q=Realtek+RTL2832U&tbm=shop
[alza]: https://www.alza.cz/evolve-mars-d198735.htm?kampan=adpla_obecna_komponenty&gclid=Cj0KEQjwjK--BRCzv-Wyu4OTosEBEiQAgFp5OChOH8GS2KgZo-VjhYVAL5O4DaUlQVfk0yV1dRpIXhMaAhh98P8HAQ#fotovideo
[czc]: https://www.czc.cz/evolveo-mars/84110/produkt?gclid=Cj0KEQjwjK--BRCzv-Wyu4OTosEBEiQAgFp5OCbP66Np11z6kO5Q1swGQNGLh2roJeC-kJok9vF_3vcaAh-08P8HAQ
[product1]: http://www.ebay.com/itm/100KHz-1-7GHz-Full-band-UV-HF-RTL-SDR-USB-Tuner-Receiver-R820T-8232-Ham-Radio-/201258847047
[product2]: https://www.amazon.com/dp/B011HVUEME/ref=as_li_ss_tl?ie=UTF8&linkCode=sl1&tag=rsv0f-20&linkId=e6b872ce4bf757ba9f71fbd35a53742e
[product3]: https://www.tsbohemia.cz/technaxx-mini-dvb-t-stick-s6_d146507.html?gclid=Cj0KEQjwjK--BRCzv-Wyu4OTosEBEiQAgFp5OBF2xOqoJUl7P0Ie5ZquUa4j7-2XCwWBxPjyI7oW9c0aArpu8P8HAQ
[tetra-listener]: https://github.com/itds-consulting/tetra-listener
[tetra-multiframe-sds]: https://github.com/itds-consulting/tetra-multiframe-sds

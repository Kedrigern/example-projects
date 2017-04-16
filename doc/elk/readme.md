# ELK

## Elastic - Logstash - Kibana

The ELK Stack is a collection of three open-source products — Elasticsearch, Logstash, and Kibana — from Elastic. Elasticsearch is a NoSQL database that is based on the Lucene search engine. Logstash is a log pipeline tool that accepts inputs from various sources, executes different transformations, and exports the data to various targets. Kibana is a visualization layer that works on top of Elasticsearch.

Together, these three different open source products are most commonly used in log analysis in IT environments (though there are many more use cases for the ELK Stack starting including business intelligence, security and compliance, and web analytics). Logstash collects and parses logs, and then Elasticsearch indexes and stores the information. Kibana then presents the data in visualizations that provide actionable insights into one’s environment.

## Alternativy

### Kibana vs Grafana

Grafana je ještě bohatší obdoba Kibany. Umí též propracované grafy, hlídat dostupnost apod. Oboje slouží k analýze a přehledu logů. Typicky úloh jako odkud k nám proudí uživatelé, co dělají apod.

### ELK vs Zabbix

[Zabbix][] je systém pro monitorování infrastruktury. Primárně hlídá věci jako zaplněnost disků, dostatek výkonu i nízkoúrovňovější věci. A na to vše napojené upozorňování. Kibana má k tomu [X-Pack][elk-allerting], ale samozřejmě je proti Zabbixu velmi omezený.

### ELK vs Kibi

[Kibi][] je *Highly configurable platform for fast, beautiful data intelligence*, čili něco kam lijeme strukturovaná (SQL, grafy, logy) i nestruktorovaná (textové dokumenty, obrázky, shluky textu) data a navzájem je propojujeme. Např. z SQL vytáhneme jména našich zákazníků a to provonáme s novinovými články. Kibi staví na ELKu.

## Instalace

Podrobný postup pro [CentOS 7][elk-centos].

1. Potřebujeme **Java 1.8**
2. Nainstalujeme **Elasticsearch**
	* DB, která poskytuje restAPI
	* běží na portu `9300`
	* v `/etc/elasticsearch/elasticsearch.yml` je `network.host: localhost` (přístup jen z localhost)
3. Nainstalujeme **Kibana**
	* webová aplikace
	* běží na portu `5601`
	* v `/opt/kibana/config/kibana.yml` je `server.host: "localhost"` (přístup jen z localhost)
4. Nainstalujeme **Logstash** a **Filebeat**
	* Filebeat zasílá logy (je přímo na monitorovaných systémech) do Logstash. Ten je rozparsuje a nahraje do Elasticsearch, aby s nimi mohla pracovat Kibana.
	* 1. důležitá věc je správně zabezpečit komunikaci mezi Filebeatem a Logstash
	* 2. důležitá věc je mít správné definice typů logů, abychom je měli správně rozparsovány
		* Definice parsování logů je v jsonech v `/etc/logstash/conf.d`
5. S konfigurací nám pomůžou předdefinované patterny pro Kibana dashboardy a Logstash parsery
	* Nachází se `https://download.elastic.co/beats/dashboards/beats-dashboards-1.1.0.zip`
	* Je v nich instalační skript `load.sh`

Díky univerzálnosti můžeme vedle Kibany nasadit Grafanu či Kibi. Důležité je, že nyní máme logy na jednom místě, kde je lze extrémně rychle a efektivně procházet.

[elk-kibana]: https://youtu.be/mMhnGjp8oOI
[elk-guide]: https://logz.io/learn/complete-guide-elk-stack/
[elk-centos]: https://www.digitalocean.com/community/tutorials/how-to-install-elasticsearch-logstash-and-kibana-elk-stack-on-centos-7
[elk-allerting]: https://www.elastic.co/products/x-pack/alerting
[Kibi]: https://siren.solutions/kibi/
[Zabbix]: http://zabbix.com

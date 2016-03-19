
# SystemD

## Základní operace s démony

Seznam procesů:
```
systemctl list-units
```

Status:
```
systemctl status httpd
● httpd.service - The Apache HTTP Server
   Loaded: loaded (/usr/lib/systemd/system/httpd.service; enabled; vendor preset: disabled)
   Active: active (running) since So 2016-03-19 17:33:21 CET; 4s ago
 Main PID: 19309 (httpd)
   Status: "Processing requests..."
   CGroup: /system.slice/httpd.service
           ├─19309 /usr/sbin/httpd -DFOREGROUND
           └─19416 /usr/sbin/httpd -DFOREGROUND
```

Start:
```
systemctl start [name]
```

Stop:
```
systemctl stop [name]
```

Povolit spuštění po startu:
```
systemctl enable crond.service
```

## Náhrada za cron

Seznam:
```
systemctl list-timers
```

http://jason.the-graham.com/2013/03/06/how-to-use-systemd-timers/

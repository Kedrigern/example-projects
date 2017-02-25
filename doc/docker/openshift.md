# OpenShift

OpenShift je enterprise distribuce Kubernetes od Red Hatu. Pomáhá nám managovat containery, primárně [Docker](docker.md).

Pomáhá nám spravovat containery, jejich množství, monitoring apod.

Skládá se z konzolového ovládání `oc` a webového rozhraní přes které ho lze ovládat.

## Slovníček

|           |        |                                                       |
|-----------|--------|-------------------------------------------------------|
| oc        | -      | cli ovládání                                          |
| rc        | replication controllers | pravidla a selektory pro containery  |
| dc        | DeploymentConfiguration | nadřazen rc                          |
| pod       | uzel   | instance containeru                                   |
| service   | služba | perzistentní služba navenek                           |
| openshift | -      | software od RH, zaobalení Kubernetes a Dockeru        |


## Lokálně

Pro spuštění lokálně je výborný [minishift][], který nám spustí opennshift v containeru lokálně. Čili si to můžeme vyzkoušet lokálně.




[minishift]: https://github.com/minishift/minishift
[rh-workshop]: http://labs-workshop-infra.cloudapps.prague.openshift3roadshow.com/roadshow

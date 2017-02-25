LVM
===

Logical Volume Manager je jakási softwarová implementace diskových oddílů.
Umožňuje měnit velikost, šifrovat etc. 

Pozor, pokud připojujete systém k systému (např. zálohu), tak může dojít ke kolizi jmen.
Pak je třeba zjistit UIID oddílu a ten přejmenovat.

Všechny operace musíme dělat pod superuživatelem.

Proskenování:

```lvmdiskscan```

Proskenování virtuálních grup:

```vgscan```

Proskenování fyzických zařízení:

```pvscan```

```vgdisplay <lvmname>```

Připojení:

```mount /dev/<lvmname> <dir-to-mount>```

Příklad 1
---------
Máme systém a chceme přimountovat jiný systém (dochází ke kolizi jmen, či chceme vybrat jen některé oddíly).

1. `pvscan` najdeme fyzická zařízení, dostaneme například:
```
PV /dev/sdb2   VG fedora_tmp   lvm2 [55,41 GiB / 0    free]
PV /dev/sda2   VG fedora       lvm2 [111,30 GiB / 64,00 MiB free]
Total: 2 [166,70 GiB] / in use: 2 [166,70 GiB] / in no VG: 0 [0   ]
```
1. `vgdisplay fedora_tmp` proskenujeme jedno konkrétní ovlast, dostaneme:
```
  --- Volume group ---
  VG Name               fedora_tmp
  System ID             
  Format                lvm2
  Metadata Areas        1
  Metadata Sequence No  7
  VG Access             read/write
  VG Status             resizable
  MAX LV                0
  Cur LV                2
  Open LV               0
  Max PV                0
  Cur PV                1
  Act PV                1
  VG Size               55,41 GiB
  PE Size               4,00 MiB
  Total PE              14184
  Alloc PE / Size       14184 / 55,41 GiB
  Free  PE / Size       0 / 0   
  VG UUID               35ul5F-trs2-Ccpx-JgCF-Z1ez-xRas-PhBgz2
```
1. Přejmenování skupiny: `vgrename 35ul5F-trs2-Ccpx-JgCF-Z1ez-xRas-PhBgz2 fedora_tmp2`

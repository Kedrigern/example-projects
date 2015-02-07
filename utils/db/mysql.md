
# Mysql

##Design, optimalization
[MySQL Workbrench](http://www.mysql.com/products/workbench) is pretty EER schema creater, SQL editor, DB connector etc. Clear choice for developmnet.

[Adminer](http://www.adminer.org) is small PHP app which allow you to compfortable access to the DB via web browser.

## Poznámky

1. První timestap dostane speciální hodnotu `CURRENT_TIMESTAMP` .
1. DELETE a SELECT nejde použít nad stejnou tabulkou.
1. mysql umí eventy (např. pravidelné promazání tabulky logů)
1. Procedury lze psát i v jiných jazycích, než SQL, ale zatím velmi omezeně. [Zdroj](http://cdn.oreillystatic.com/en/assets/1/event/2/A%20Tour%20of%20External%20Language%20Stored%20Procedures%20for%20MySQL%20Presentation.pdf
1. MySQL LIKE etc. funkce mohou nerozlišovat velikost písměn (což je zbytečné, když existuje ILIKE), ale hlavně mohou správně ignorovat diakritiku. Je k tomu třeba nastavit kódování na `utf8_general_ci`


## Typy tabulek

`InnoDB` podoporuje klíče, vícesloupcové indexy etc.

`ARCHIVE` je komprimovaný, podporuje jen vkládání.

`BLACKHOLE` podporuje vše, ale nic neukládá, tudíž se dá použít pro testování či vyprázděnní tabulky typu `ARCHIVE`.

## CLI
`mysqlimport --local -u <user> -p<heslo> --fields-terminated-by=, --default-character-set=utf8 category <tablename>.csv`



##Triggers

* [Error](http://stackoverflow.com/questions/24/throw-an-error-in-a-mysql-trigger):
```sql
declare msg varchar(255);
if new.id < 0 then
 set msg = concat('MyTriggerError: Trying to insert a negative value in trigger_test: ', cast(new.id as char));
 signal sqlstate '45000' set message_text = msg;
end if;
```

### Examples

* one from two column can be filled (second is null):
```sql
begin
	if (new.name1 IS NULL and new.name2 IS NULL) or (new.name1 IS NOT NULL and new.name2 IS NOT NULL) then
		signal sqlstate '45000' set message_text = 'Only one of the columns (`name1`, `name2`) can be filled.';
	end if;
end;
```

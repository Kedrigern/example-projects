
# Mysql

##Design, optimalization
[MySQL Workbrench](http://www.mysql.com/products/workbench) is pretty EER schema creater, SQL editor, DB connector etc. Clear choice for developmnet.

[Adminer](http://www.adminer.org) is small PHP app which allow you to compfortable access to the DB via web browser.

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

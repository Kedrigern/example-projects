
# Flask

## Jinja

LOOP - rekurze

```jinja
{% set outer_loop = loop %}
{% for key in category recursive %}
	{{ key }}
	{{ loop( key.children ) }}
{% endfor %}
```

## Libtree

Obecná práce nad stromy za využití PostgreSQL

## Odkazy

ZODB.org

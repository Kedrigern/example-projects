# Jekyll

Je aplikace napsaná v ruby, která z předdefinovaných šablon vygeneruje statickou
stránku. Tím pádem dovoluje tvořit i trochu složitější weby (např. blogy,
firemní prezentace) bez nutnosti jakýhkoliv nároků na hosting. Navíc je nativně
podporován Github pages, čili vše můžete hostovat na Githubu.

## Github pages

## Struktura

```
├── about.md                -- statická stránka
├── _config.yml             -- konfigurační soubor
├── css                         
│   └── main.scss
├── feed.xml                -- atom feed             
├── _includes               -- snippety stránky
│   ├── footer.html         -- patička stránky
│   ├── header.html         -- hlavička stránky
│   └── head.html           -- meta hlavička stránky
├── index.html              
├── _layouts                -- různé druhy layoutů
│   ├── default.html
│   ├── page.html
│   └── post.html
├── _posts                  -- příspěvky v markdown s metadaty
│   ├── people-ondrej-profant.md
│   ├── 2016-02-12-another-post.md
│   └── 2016-02-13-welcome-to-jekyll.md
├── _sass
│   ├── _base.scss
│   ├── _layout.scss
│   └── _syntax-highlighting.scss
└── _site                   -- zkompilovaná stránka
```

[Dokumentace](http://jekyllrb.com/docs/structure/)

## Tipy

### Vypsání jen určitých kategorii

```html
<ul class="posts">
{% for post in site.posts %}
    {% if post.categories contains 'demography' %}
        <li><span>{{ post.date | date_to_string }}</span> &raquo; <a href="{{ BASE_PATH }}{{ post.url }}">{{ post.title }}</a></li>
    {% endif %}
{% endfor %}
</ul>
```

# Angular 2 

Angular 2 je rozdílný oproti Angularu 1. Je psán v typescriptu, čili je silně typovaný a vychází z ES6. Organizačně rozlišuje pouze:

- komponenty (bývalé controllery): mají styl, šablonu a kód
- service (model): obvykle komunikují se světem (http, localfiles, složité transformace)
- samostatné třídy (model): třídy našeho modelu (User apod)

Struktura je relativně složitá a míra provázanosti souborů velká a proto se používá angular-cli, což je cmd utilita, která nám pomáhá:

- vytvořit nový projekt `ng new [--minimal] <name>`
- běh aplikace `ng serve [-o]`
- kompilaci aplikace pro produkci `ng`
- přidat komponentu: `ng`
- přidat service `ng`
- apod 

Velmi dobrý [tutorial][] a [cheat sheet][]. Podrobnější vysvětlení [http][http example]. Pro vývoj se velmi hodí mít lokální [json server], který nám umožní snadno simulovat data.

[tutorial]: https://www.barbarianmeetscoding.com/blog/2016/03/25/getting-started-with-angular-2-step-by-step-1-your-first-component/
[cheat sheet]: https://www.cheatography.com/gregfinzer/cheat-sheets/angular-2/
[http example]: http://www.concretepage.com/angular-2/angular-2-http-get-example
[json server]: https://github.com/typicode/json-server

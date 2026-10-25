# vlabidem

Web účetní kanceláře VLABIDEM s.r.o., [www.vlabidem.cz](http://www.vlabidem.cz/).

Statické HTML stránky s [Bootstrapem 5](https://getbootstrap.com/) (lokální kopie, bez jQuery).
Nic se nesestavuje: co je v repozitáři, nahrává se na hosting.

## Struktura

| Soubor | Obsah |
|---|---|
| `index.html` | hlavní stránka |
| `taxes.html`, `economy.html`, `wages.html` | služby: daně, účetnictví, mzdy |
| `commissions.html` | provize za doporučení |
| `links.html` | užitečné odkazy |
| `contacts.html` | kontakty, údaje z obchodního rejstříku, mapa |
| `ochrana-osobnich-udaju.html` | ochrana osobních údajů |
| `404.html` | stránka „nenalezeno“ |
| `style.css`, `sticky-footer-navbar.css` | vlastní styly |
| `.htaccess` | konfigurace Apache (chybová stránka, přesměrování) |
| `robots.txt`, `sitemap.xml` | pro vyhledávače |

Menu a patička jsou zkopírované v každé stránce – při změně je upravte všude.

## Nasazení

Hosting Yellowpoint, FTP `host4.yellowpoint.cz`, web je v adresáři `/web`. Server podporuje jen FTPS:

```sh
curl --ssl-reqd -u UZIVATEL -T soubor.html ftp://host4.yellowpoint.cz/web/soubor.html
```

Nahrávají se jen soubory webu (ne `README.md`, `LICENSE`, `.gitignore`).
Do repozitáře se mění přes pull requesty a na web se nahrává až sloučený `master`.

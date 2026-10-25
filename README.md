# vlabidem

Web účetní kanceláře VLABIDEM s.r.o., [www.vlabidem.cz](http://www.vlabidem.cz/).

Statické HTML stránky s [Bootstrapem 5](https://getbootstrap.com/) (lokální kopie, bez jQuery).
Na serveru neběží nic než Apache se statickými soubory.

## Úpravy stránek

Menu, hlavička a patička jsou jen jednou v `src/layout.html`, obsah každé
stránky v `src/pages/<stránka>.html` (nahoře titulek a popis pro vyhledávače).
Stránky v kořeni repa se z nich generují **lokálně**:

```sh
python3 build.py          # přegeneruje stránky v kořeni
python3 build.py --check  # jen ověří, že jsou aktuální
```

Stačí Python 3 bez dalších balíčků. Vygenerované stránky se commitují;
na server se nahrávají ony, ne `src/` ani `build.py` (`.htaccess` je i tak blokuje).
Nová stránka do menu: doplnit ji do `NAV` v `build.py`.

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

## Nasazení

Hosting Yellowpoint, FTP `host4.yellowpoint.cz`, web je v adresáři `/web`. Server podporuje jen FTPS:

```sh
curl --ssl-reqd -u UZIVATEL -T soubor.html ftp://host4.yellowpoint.cz/web/soubor.html
```

Nahrávají se jen soubory webu (ne `src/`, `build.py`, `README.md`, `LICENSE`, `.gitignore`).
Do repozitáře se mění přes pull requesty a na web se nahrává až sloučený `master`.

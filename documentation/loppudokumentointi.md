# Jäsenrekisteri

Jäsenrekisterin tarkoituksena on pitää kirjaa seuran jäsenistä ja seurata harjoitusaktiivisuutta. Jäsenet (, joille on luotu käyttäjä) pääsevät tarkastelemaan tietoja ja muuttamaan omia tietojaan. Pääkäyttäjät/valmentajat pääsevät muuttamaan ja tarkastelemaan myös muiden tietoja.

## Käyttöohje
Sovellus vaatii kirjautumisen.

Sovelluksessa navigointi hoituu pääasiassa yläpalkissa olevan valikon avaulla. Mikäli näyttö on pieni, valikko romahtaa ja sen saa uudestaan auki painamalla ikonia yläpalkissa. Navigointipalkkia täydentävät sivuilla olevat linkit ja painikkeet. Painikkeet on pyritty nimeämään mahdollisimman loogisesti, jotta niiden käyttäminen olisi intuitiivista.

Käyttäjälle on näkyvissä vain sellaiset toiminnot, joita hänellä on oikeus käyttää.

## Peruskäyttäjä 
Pääsee katsomaan seuran jäseniä ja ryhmiä. Molemmista näkymistä ryhmän nimeä klikkaamalla pääsee katsomaan ryhmän lisätietoja. Ryhmän lisätiedoissa kerrotaan jäsenmäärä, ryhmän jäsenten harjoituskertojen summa ja seuran ohjaajien yhteystiedot.

Jäsenlistauksesta pääsee muokaamaan omia tietojaan painamalla modify-painiketta oman tietueensa kohdalla. Omista tiedoista pääsee edelleen muokkaamaan omaa käyttäjäänsä eli vaihtamaan käyttäjätunnusta tai salasanaa.

Jäsenlistauksesta pääsee myös tarkastelemaan omia harjoituskäyntejään painamalla practices-painiketta. Alle kuukauden vanhoja harjoituksia voi myös poistaa. Käyttä voi myös lisätä itselleen uusia harjoituskäyntejä (ainakin toistaiseksi).

## Pääkäyttäjä
Pääsee käsiksi kenen tahansa tietoihin edellä kuvatulla tavalla. Lisäksi pääkäyttäjä voi lisätä ryhmiä ja poistaa tyhjiä ryhmiä sekä lisätä ja poistaa käyttäjiä. Ryhmän sivulta pääkäyttäjä pääsee lisäämään harjoituskäyntejä koko ryhnmälle kerralla. (Ryhmäkohtainen harjoituskäyntien lisäys voisi olla valmentajan aloitusnäyttönä). 

Pääkäyttäjä voi tehdä toisista käyttäjistä pääkäyttäjiä muuttamalla jäsenen tilin asetuksia. Pääkäyttäjä voi myös luoda jäsenille tilin jäsenrekisteriin. Tilin asetuksia pääsee muokkaamaan jäsenen lisätiedoista.

## Asennusohje

### Demo
[demo](https://polar-plains-24269.herokuapp.com/)

pääkäyttäjä: admin, admin
peruskäyttäjä: testi, testi

[Asennusohje](https://github.com/tuomasmk/jasenrekisteri/blob/master/documentation/Asennusohje.md)


## Sovelluksen rajoitteet, kehityskohteet, puuttuvat ominaisuudet
* Sovelluksen taulukot ovat staattisia, eikä niitä pysty järjestämään eri sarakkeiden mukaan.
* Osa sovelluksen toiminnallisuuksista on turhan monen klikkauksen takana.
* Toiminnallisuuksien jakamista peruskäyttäjien ja pääkäyttäjien välillä pitäisi parantaa.
* Virheilmoitus ei aina ole kovin informatiivinen, mikäli käyttäjä yrittää mennä suoraan osoitteeseen, johon hänellä ei ole riittäviä oikeuksia.
* Salasanat selväkielisinä
* Käyttäjän ja jäsenen integroiminen toisiinsa paremmin. Toisaalta on hyvä voida olla käyttäjiä, jotka eivät ole jäseniä.
* Käyttäjän pitäisi voida kuulua useampaan ryhmään samaan aikaan. Lisäksi käyttäjällä pitäisi olla ryhmässä jokin rooli (valmentaja, apuvalmentaja, harjoittelija). Tällä hetkellä pääkäyttäjät ovat ryhmän valmentajia.

## Kokemuksia
Uusien kirjastojen määrä aiheutti hyvin jyrkän oppimiskäyrän ja useammassa kohdassa tuli kiivettyä takapuoli edellä puuhun, ennen kuin sisäisti kirjastojen ominaisuuksia riittävästi. Samasta syystä ohjeiden etsiminen oli vaikeaa, kun ei aina ollut selvää mihin komponenttiin vika liittyi. Todennäköisesti päädyin myös kirjoittamaan liian paljon sql:ää, vaikka kirjastot olisivat tarjonneet samoja toiminnallisuuksia valmiina. Myös pythonin käytöstä on kulunut sen verran aikaa, että syntaksia joutui muistelemaan ennen kun se jälleen sujui.

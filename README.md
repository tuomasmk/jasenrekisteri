# Jäsenrekisteri/harjoituskäyntiseuranta

Sovelluksella pidetään kirjaa urheiluseuran jäsenistä. Jäsenistä kerätään erilaista tietoa, kuten vyöarvokorotukset, koulutukset, harjoitusryhmät ja harjoituskäynnit. Tietoja voidaan tarkastella käyttöoikeuksista riippuen erilaisten yhteenvetonäkymien avulla.

[demo](https://polar-plains-24269.herokuapp.com/)

tunnukset: username = testi, password = testi

admin-tunnukset: username = admin, password = admin

[asennusohje](https://github.com/tuomasmk/jasenrekisteri/blob/master/documentation/Asennusohje.md)

[tietokantakaavio](https://github.com/tuomasmk/jasenrekisteri/blob/master/documentation/tietokantakaavio.png)

[käyttötapaukset](https://github.com/tuomasmk/jasenrekisteri/blob/master/documentation/userstories.md)


## Ominaisuudet
* Kirjautumistoiminnallisuus, jossa kaksi roolia: tavallinen käyttäjä ja pääkäyttäjä
* Toimintojen näkyvyyttä on rajattu käyttöoikeuksien mukaan.

### Peruskäyttäjän toiminnallisuudet
* Voi lisätä ja tarkastella jäseniä ja muuttaa omia tietojaan.
* Voi tarkastella ryhmiä (listaus ja lisätiedot).
* Jäsen kuuluu johonkin ryhmään ja jäsenelle voi lisätä harjoituskäyntejä joko yksittäin tai ryhmän sisällä useammalle kerralla.
* Alle kuukauden vanhoja omia harjoituskäyntejä voi poistaa.
* Ryhmien yhteenvedossa näkyy ryhmän jäsenten määrät.
* Jäsenen tiedoissa näkyy harjoituskertojen saldo (yhteenvedossa).

### Pääkäyttäjän toiminnallisuudet edellisten lisäksi
* Voi lisätä ryhmiä ja poistaa tyhjiä.
* Voi poistaa jäseniä, samalla poistuvat yksittäiset harjoituskerrat.
* Voi luoda jäsenelle käyttäjän.
* Voi tehdä jäsenestä pääkäyttäjän.
* Voi lisätä harjoituskäyntejä yksittäin tai ryhmässä.
* Jäsenen voi siirtää ryhmästä toiseen.

### Kehityskohteita
* Kävijämääristä voi tehdä tilastoja.
* Harjoituskäynnin pituuden hyödyntäminen.

# Jäsenrekisteri/harjoituskäyntiseuranta

Sovelluksella pidetään kirjaa urheiluseuran jäsenistä. Jäsenistä kerätään erilaista tietoa, kuten vyöarvokorotukset, koulutukset, harjoitusryhmät ja harjoituskäynnit. Tietoja voidaan tarkastella käyttöoikeuksista riippuen erilaisten yhteenvetonäkymien avulla.

[demo](https://polar-plains-24269.herokuapp.com/)

tunnukset: username = testi, password = testi

admin-tunnukset: username = admin, password = admin

[käyttö-/asennusohje](https://github.com/tuomasmk/jasenrekisteri/blob/master/user_guide.md)

[tietokantakaaviohahmotelma](https://github.com/tuomasmk/jasenrekisteri/blob/master/documentation/tietokantakaavio.jpg)

[käyttötapaukset](https://github.com/tuomasmk/jasenrekisteri/blob/master/documentation/userstories.md)


## Ominaisuudet
* Kirjautumistoiminnallisuus, jossa kaksi roolia: tavallinen käyttäjä ja pääkäyttäjä

### Peruskäyttäjän toiminnallisuudet
* Voi lisätä ja tarkastella jäseniä (myöhemmin muuttaa omia tietoja).
* Voi tarkastella ryhmiä (ja ainakin vielä, poistaa tyhjiä ryhmiä).
* Jäsen kuuluu johonkin ryhmään ja jäsenelle voi lisätä harjoituskäyntejä joko yksittäin tai ryhmän sisällä useammalle kerralla.
* Alle kuukauden vanhoja harjoituskäyntejä voi poistaa.
* Ryhmien yhteenvedossa näkyy ryhmän jäsenten määrät.
* Jäsenen tiedoissa näkyy harjoituskertojen saldo.

### Pääkäyttäjän toiminnallisuudet
* Voi lisätä ryhmiä ja poistaa (ainakin) tyhjiä.
* Voi poistaa jäseniä, samalla poistuvat yksittäiset harjoituskerrat.

### Kehityskohteita
* Kävijämääristä voi tehdä tilastoja.
* Jäsenen tietoja voi muokata (käyttäjä omia, pääkäyttäjä kaikkia).
* Pääkäyttäjät voivat siirtää henkilöitä ryhmästä toiseen.
* Harjoituskäynnille pituus.

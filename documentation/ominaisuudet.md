# Ominaisuudet/käyttötapaukset
* Kirjautumistoiminnallisuus, jossa kaksi roolia: tavallinen käyttäjä ja pääkäyttäjä
* Toimintojen näkyvyyttä on rajattu käyttöoikeuksien mukaan.

## Peruskäyttäjän toiminnallisuudet
* Voi lisätä ja tarkastella jäseniä ja muuttaa omia tietojaan.
* Voi tarkastella ryhmiä (listaus ja lisätiedot).
* Jäsen kuuluu johonkin ryhmään ja jäsenelle voi lisätä harjoituskäyntejä joko yksittäin tai ryhmän sisällä useammalle kerralla.
* Alle kuukauden vanhoja omia harjoituskäyntejä voi poistaa.
* Ryhmien yhteenvedossa näkyy ryhmän jäsenten määrät.
* Jäsenen tiedoissa näkyy harjoituskertojen saldo (yhteenvedossa).

## Pääkäyttäjän toiminnallisuudet edellisten lisäksi
* Voi lisätä ryhmiä ja poistaa tyhjiä.
* Voi poistaa jäseniä, samalla poistuvat yksittäiset harjoituskerrat.
* Voi luoda jäsenelle käyttäjän.
* Voi tehdä jäsenestä pääkäyttäjän.
* Voi lisätä harjoituskäyntejä yksittäin tai ryhmässä.
* Jäsenen voi siirtää ryhmästä toiseen.

## Kehityskohteita
* Kävijämääristä voi tehdä tilastoja.
* Harjoituskäynnin pituuden hyödyntäminen.

## Tarvittavat SQL-lauseet

### Ryhmän jäsenten hakeminen
```
SELECT groups.id, groups.name,
member.id, member.firstnames, member.lastname
FROM groups LEFT JOIN member
ON member.group_id = groups.id
WHERE groups.id = :id
ORDER BY member.lastname
```

### Ryhmän jänsenten harjoituskäyntien summa
```
SELECT COUNT(practice.id)
FROM practice WHERE practice.member_id IN
(SELECT member.id from member
WHERE member.group_id=:id)
```

### Ryhmän valmentajien hakeminen
Valmentajuuden ehtona on, että käyttäjä kuuluu ryhmään ja on pääkäyttäjä.

```
SELECT member.lastname, member.firstnames,
member.\"phoneNumber\" FROM member
WHERE member.group_id=:id
AND member.id IN
(SELECT account.member_id FROM account
WHERE account.id IN
(SELECT role.user_id FROM role
WHERE role.name='ADMIN'))
```

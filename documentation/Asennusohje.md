# Asennusohje

Sovelluksen lataaminen omalle koneelle onnistuu komennolla:

`git clone git@github.com:tuomasmk/jasenrekisteri.git`


## Paikallinen asennus

Seuraavat komennot suoritetaan juuri ladatun sovelluksen juurihakemistossa.

virtuaaliympäristön asennus komennolla:

`python3 -m venv venv`

venv aktivoidaan komennolla:

`source venv/bin/activate`

projektin tarvitsemat riippuvuudet asentuvat projektin juurihakemistossa komennolla:

`pip install -r requirements.txt`

ja lopulta projektin käynnistäminen suorittamalla juuresta löytyvä run.py tiedosto:

`python3 run.py`


## Asennus herokuun

Seuraavat komennot suoritetaan juuri ladatun sovelluksen juurihakemistossa.

kirjaudutaan herokuun komennolla:

`heroku login`

luodaan uusi sovellus herokuun komennolla:

`heroku create`

lisätään PostgreSQL herokuun komennolla:

`heroku addons:add heroku-postgresql:hobby-dev`

viedään sovellus herokuun:

`git push heroku master`


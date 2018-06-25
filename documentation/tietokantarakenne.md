# Tietokantarakenne
Tietokannan rakenne on kuvattu [tietokantakaaviossa](https://github.com/tuomasmk/jasenrekisteri/blob/master/documentation/tietokantakaavio.png).
Tietokanta on pääosin normalisoitu, ainoa poikkeus on käyttäjän sisältämä nimi, joka on päällekkäinen jäsenen tietojen kanssa. Poikkeus johtu siitä, että käyttäjä voi olla olemassa ilman jäsentä.

Create table lauseet:
```
CREATE TABLE grade (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(6) NOT NULL, 
	color VARCHAR(20) NOT NULL, 
	PRIMARY KEY (id)
)
```

```
CREATE TABLE groups (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id)
)
```

```
CREATE TABLE member (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	firstnames VARCHAR(144) NOT NULL, 
	lastname VARCHAR(144) NOT NULL, 
	email VARCHAR(144), 
	"phoneNumber" VARCHAR(20), 
	address VARCHAR(144), 
	"postalCode" VARCHAR(20), 
	country VARCHAR(20), 
	city VARCHAR(144), 
	group_id INTEGER NOT NULL, 
	grade_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(group_id) REFERENCES groups (id), 
	FOREIGN KEY(grade_id) REFERENCES grade (id)
)
```

```
CREATE TABLE practice (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	date DATE NOT NULL, 
	duration INTEGER, 
	member_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(member_id) REFERENCES member (id)
)
```

```
CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	member_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(member_id) REFERENCES member (id)
)
```

```
CREATE TABLE role (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(20) NOT NULL, 
	user_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(user_id) REFERENCES account (id)
)
```

# Keskustelusovellus Ulina
Sovelluksessa näkyy keskustelualueita, joista jokaisella on tietty aihe. Alueilla on keskusteluketjuja, jotka muodostuvat viesteistä. Jokainen käyttäjä on peruskäyttäjä tai ylläpitäjä.

### Sovelluksen ominaisuuksia:

- Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen.
- Käyttäjä näkee sovelluksen etusivulla listan alueista sekä jokaisen alueen ketjujen ja viestien määrän.
- Käyttäjä voi luoda alueelle uuden ketjun antamalla ketjun otsikon ja aloitusviestin sisällön.
- Käyttäjä voi kirjoittaa uuden viestin olemassa olevaan ketjuun.
- Käyttäjä voi muokata luomansa ketjun otsikkoa sekä lähettämänsä viestin sisältöä. Käyttäjä voi myös poistaa ketjunsa tai viestinsä.
- Käyttäjä voi etsiä keskustelualueelta kaikki viestit, joiden osana on annettu sana.
- Käyttäjä voi etsiä toisen käyttäjän lähettämät viestit.
- Käyttäjä voi antaa "Yah" tai "Nah" ääniä viesteille.

Sovellusta voi käyttää vain paikallisesti. Käynnistysohjeet ovat alla:
1. Lataa Ulina tiedostot GitHubista.
2. Pura tiedostot.
3. Siirry tiedoston juurikansioon ja luo .env tiedosto, jonka sisältö on:
```bash
DATABASE_URL=<tietokannan-paikallinen-osoite>
SECRET_KEY=<salainen-avain>
```
4. Suorita seuraavat komennot:
```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r ./requirements.txt
$ psql < schema.sql
```
5. Suorita uudella terminaalilla komento:
```bash
$ start-pg.sh
```
6. Sovellus on nyt valmiina käytettäväksi alkuperäisellä terminaanilla komennolla: 
```bash
$ flask run
```
### Välipalautus 2
Tällä hetkellä sovelluksessa voi luoda uuden tunnuksen ja kirjautua vanhalle tunnukselle. Etusivulla näkyvät kaikki aiheet, joita on tällä hetkellä vain kolme, sekä sovellukseen lähetetyt viestit. Aihetta painamalla käyttäjä näkee kaikki viestit, jotka on lähetetty siihen aiheeseen.

### Välipalautus 3
Keskusteluaiheita lisätty, ulkonäköä päivitetty ja sivuihin on lisätty linkit muihin sivuihin, jotka mahdollistivat helpomman selaamisen.

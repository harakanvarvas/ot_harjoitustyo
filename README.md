## Selkärangattoman aikuistumisen ajankohdan arvioija

Tällä hetkellä sovellus arvioi aikuistumisen päivän tarkkuudella. Muutetaan myöhemmin viikon 
tarkkuuteen, sillä tarkkaa päivää on käytännössä mahdotonta arvioida täsmällisesti. Aikuistumisarvio
viikon tarkkuudella antaa todennäköisesti realistisemmat valmiudet varautua viimeiseen nahanluontiin
ja muuttaa esimerkiksi terraario-olosuhteita hyvissä ajoin nahanluontiin sopivaksi.



### Dokumentaatio
[changelog](https://github.com/harakanvarvas/ot_harjoitustyo/blob/master/harjoitustyo/dokumentaatio/changelog.md)

[arkkitehtuuri](https://github.com/harakanvarvas/ot_harjoitustyo/blob/master/harjoitustyo/dokumentaatio/arkkitehtuuri.md)

[määrittelydokumentti](https://github.com/harakanvarvas/ot_harjoitustyo/blob/master/harjoitustyo/dokumentaatio/vaatimusmaarittely.md)

[tuntikirjanpito](https://github.com/harakanvarvas/ot_harjoitustyo/blob/master/harjoitustyo/dokumentaatio/tyoaikakirjanpito.md)



### Komentorivitoiminnot


##### Sovelluksen käynnistäminen tapahtuu komennolla
```
poetry run invoke start
```

##### Testien ajaminen tapahtuu komennolla
```
poetry run invoke test
```

##### Testikattavuuden kerääminen ja HTML-tiedoston muodostaminen tapahtuu komennolla
```
poetry run invoke coverage-report
```

##### Pylintin laatutarkistuksen suorittaminen tapahtuu komennolla
```
poetry run invoke lint
```

# pw2 ListView

Tämä raportti on Tero Karvisen ohjaaman [Python Web Service From Idea to Production](https://terokarvinen.com/2021/python-web-service-from-idea-to-production-2022/#pw1-hello-dj-a) kurssin toisen päivän tehtäviin.

## A. Tee alusta lähtien uusi Django-projekti. Tee siihen sivu, joka listaa tietueita tietokannasta ilman kirjautumista. Valitse jokin muu aihe kuin aiemman esimerkin CRM. Aivan simppeli esimerkkiprojekti riittää, mutta valitse sille jokin esimerkkiaihe.

Ajatuksenani oli tehdä projekti jolla voidaan listata eri viinejä.

Aloitetaan käynnistämällä virtualenv `source env/bin/activate` ja luomalla uusi projekti komennolla. `django-admin startproject wineshop`  Tehdään myös migraatiot, että saadaan valmis admin-paneeli meidän weppisivulle. `./manage.py makemigrations` `./manage.py migrate`
![image](pw2/pics/alkupw2.jpg)
Luodaan vielä superuser, että pääsemme käsiksi juuri luotuun paneeliin. `./manage.py createsuperuser` ja lisäksi luodaan uusi taulu meidän tietokantaan. `./manage.py startapp winelist` `micro wineshop/settings.py`
![Image](pw2/pics/sudojaapp.jpg)
![Image](pw2/pics/settingswine.jpg)
Luodaan meille uusi viini olio, ajetaan migraatiot ja katsotaan tilanteen toimivuus (jonka olisi pitänyt tehdä aikaisemmin jo mutta unohtui).
![Image](pw2/pics/models.jpg)
![Image](pw2/pics/run.jpg)
![Image](pw2/pics/test.png)



## B. Palauta työ Laksuun. Arvioi kahden muun opiskelijan palautus Laksussa. (tätä alakohtaa ei tarvitse raportoida) 

## C. Vapaaehtoinen: kokeile tehdä pari samantapaista projektia. Osaatko tehdä ulkomuistista? Kirjaa kohdat, jotka piti katsoa materiaalista, niin näät, mitä vielä pitää kerrata.

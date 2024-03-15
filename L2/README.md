# Laboratorinis darbas Nr. 2. Sprendinių medžiai ir atsitiktiniai miškai

## Laboratorinio darbo nefunkciniai reikalavimai:
* Sprendimų medžio algoritmas kuriamas naudojant _Python_ programavimo kalbą;
* Darbo galutinį vertinamąjį balą sudaro darbo gynimas ir ataskaita. Galutinis balas taip pat priklauso nuo darbo išpildymo lygio, t.y. kiek funkcinių reikalavimų (pateikti žemiau) yra realizuota bei nuo jų korektiškumo;
* Prieš ginantis darbą turi būti pateikta laboratorinio darbo ataskaita (el.forma) Moodle sistemoje;

## Funkciniai darbo reikalavimai:
1. Pasirinkite duomenų rinkinį kuriam sudarysite sprendinių medį.
2. Kaip sprendimų medžio išvestį pasirinkite prognazuojamą atributą (_Patariama pasirinkti kategorinį kintąmąjį, kurio kardinalumas yra nuo 4 iki 10_).
3. Turimą duomenų rinkinį suskaidykite į apmokymo bei testavimo poaibius. Apmokymo aibė turi būti didesnė nei testavimo.
4. Suskaidykite duomenų poaibius į įvestis ir išvestis.
5. Naudojant apmokymo duomenų rinkinį, sudarykite sprendimų medį. Galime rinktis iš keleto algoritmų `ID3`, `C4.5`, `CART` arba pan. Nuo to priklauso kokius indeksus/metodus naudosite medžio dalijimui (pvz. `Gini`, `Entropy`, `Gain` ir t.t.). Žinoti koks yra skirtumas tarp šių algoritmų ir dalijimo indeksų.
6. Grafiškai atvaizduokite gautą sprendimų medį. Atvaizdavimui galima naudoti `slearn` ir `graphviz` arba kitas bibliotekas. Jei sudarytas sprendimų medis yra labai didelis, kad payktų įskaitomai pateikti ataskaitoje - įkelkite failą atskirai ir ataskaitoje pateikite tik medžio fragmentą ir komentarus apie gautą struktūrą.
7. Ištestuokite sudarytą sprendimų medį naudojant testavimo duomenis ir apskaičiuokite prognozavimo tikslumą/paklaidą. Nurodykite kokią paklaidos materiką skaičiuojate (pvz., `MAE`, `MSE` ir t.t.). Taip pat klasifikavimo uždaviniui pateikite susimaišymo (angl. _confusion_) matricą.
8. Keičiant maksimalų medžio gylį, ekspermentiniu būdu išmatuokite skirtingų gylių (3-4 variacijos) medžių formavimo trukmę bei gaunamą tikslumą, t.y. medžio augimas stabdomas nuo tam tikro gylio. Rezultatus pateikite ataskaitoje.
9. Naudojant tą patį apmokymo ir testavimo duomenų imties pasiskirtymą kaip ir formuojant sprendimų medį, suformuokite atsitiktinį mišką kurį sudaro 5 medžiai. Ataskaitoje pateikti jų skirtumus. Maksimalus medžio gylis - gylis užfiksuotas eksperimento metu, kuris pateikė geriausius rezultatus.
10. Keičiant mišką sudarančių medžių kiekį [3-9], nustatykite geriausius rezultatus pateikiantį atsitiktinį mišką.
11. Palyginkite pirminio sprendimų medžio ir atsitiktinio miško gautus rezultatus.
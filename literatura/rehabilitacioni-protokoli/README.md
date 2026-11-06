# MFS Masterklas | Biblioteka rehab protokola

Ovo je **indeks originalnih strucnih izvora**, sa direktnim linkovima ka PDF dokumentima kada su dostupni. Provera javnih linkova: **6. novembar 2026**.

**Vazno:** repozitorijum `Nidza22/Mfs-masterklas` je javan. Originalni PDF-ovi nisu kopirani u javni repozitorijum bez individualne provere uslova redistribucije. Skripta `download.py` preuzima javne PDF-ove **lokalno, samo za strucno proucavanje**, a `.gitignore` sprecava slucajan commit.

## Izvori po regijama

### KOLENO I PATELARNA TETIVA

| Dokument | Izdavac | Pristup |
|---|---|---|
| [ACL rekonstrukcija - kompletan protokol (33 str.)](https://www.nevpt.com/pdf/ACL%20v.%205.0%20Master.pdf) | Nevada Physical Therapy | Direktan PDF |
| [ACL - skracena verzija (5 str.)](https://www.nevpt.com/pdf/ACL%20v.%205.0%20Short%20Form.pdf) | Nevada Physical Therapy | Direktan PDF |
| [ACL rekonstrukcija - smernice, izdanje april 2021 (19 str.)](https://cpb-us-w2.wpmucdn.com/sites.udel.edu/dist/c/3448/files/2016/01/UDPT-ACL-Rehab-Guideline-REVISED.pdf) | University of Delaware | Direktan PDF |
| [Totalna artroplastika kolena TKA (5 str.)](https://cpb-us-w2.wpmucdn.com/sites.udel.edu/dist/c/3448/files/2016/01/TKA-Protocols-updated-3_2021.pdf) | University of Delaware | Direktan PDF |
| [Patelarna tendinopatija - tretman i progresija (jul 2016)](https://sites.udel.edu/ptclinic/files/2016/10/Patellar-Tendinopathy-Treatment-Protocol-21sjaim-yi2e4k.pdf) | University of Delaware | Direktan PDF |
| [ACL rekonstrukcija - 2023 evidence-based clinical guideline (open access na PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11785408/) | Aspetar / BJSM | Otvorena stranica |
| [Aspetar ACL Rehabilitation Protocol - besplatno uz formular](https://www.aspetar.com/en/professionals/aspetar-clinical-guidelines/acl-rehabilitation-protocol) | Aspetar | Formular / eBook |
| [Practitioner's Guide to ACL - besplatan eBook uz formular](https://resources.valdhealth.com/practitioners-guide-to-acl) | VALD | Formular / eBook |

### KUK, PREPONE I ADUKTORI

| Dokument | Izdavac | Pristup |
|---|---|---|
| [Artroskopija kuka - postoperativna rehabilitacija (18 str.)](https://www.nevpt.com/pdf/Hip%20Arthro%20Master%20%28final%29.pdf) | Nevada Physical Therapy | Direktan PDF |
| [Acute Adductor Injuries - Treatment Protocol](https://www.aspetar.com/AspetarFILEUPLOAD/UploadCenter/637316240569681376_Acute%20adductor%20injuries%20-%20Aspetar%20Treatment%20protocol.pdf) | Aspetar | Direktan PDF |
| [Practitioner's Guide to Osteoarthritis and Joint Replacements - uz formular](https://resources.valdperformance.com/practitioners-guide-to-osteoarthritis-and-joint-replacements) | VALD | Formular / eBook |

### RAME

| Dokument | Izdavac | Pristup |
|---|---|---|
| [Bankart repair - postoperativni protokol (4 str.)](https://bpb-us-w2.wpmucdn.com/sites.udel.edu/dist/c/3448/files/2016/01/Bankart-Repair.pdf) | University of Delaware | Direktan PDF |
| [Rotator cuff repair - manje rupture bez retrakcije (2 str.)](https://bpb-us-w2.wpmucdn.com/sites.udel.edu/dist/c/3448/files/2016/10/RC_uncomplicated_2015-2dim2nf.pdf) | University of Delaware | Direktan PDF |
| [Rotator cuff repair - velike rupture sa retrakcijom (4 str.)](https://cpb-us-w2.wpmucdn.com/sites.udel.edu/dist/c/3448/files/2017/07/updated-large-RTC-with-retraction-guidelines-Jul-21-2017-re5zvc.pdf) | University of Delaware | Direktan PDF |
| [Rotatorna manzetna - narativni pregled (nije klasicni fazni protokol; 7 str.)](https://www.nevpt.com/pdf/Rotator%20Cuff%20Repair%20Rehabilitation.pdf) | Nevada Physical Therapy | Direktan PDF |

### ZADNJA LOZA

| Dokument | Izdavac | Pristup |
|---|---|---|
| [Aspetar Hamstring Protocol (veliki PDF, ~12.6 MB)](https://www.aspetar.com/aspetarfileupload/UploadCenter/636209313253275549_aspetar%20Hamstring%20Protocol.pdf) | Aspetar | Direktan PDF |
| [Aspetar Hamstring Injury Rehabilitation Pathway - besplatno uz formular](https://www.aspetar.com/en/professionals/aspetar-clinical-guidelines/hamstring-injury-rehabilitation-pathway) | Aspetar | Formular / eBook |

### LIST I AHILOVA TETIVA

| Dokument | Izdavac | Pristup |
|---|---|---|
| [Practitioner's Guide to the Calf & Achilles Complex - uz formular](https://resources.valdperformance.com/practitioners-guide-to-the-calf-achilles-complex) | VALD | Formular / eBook |

## Kako lokalno preuzeti javne PDF-ove

1. Preuzmi/kloniraj repozitorijum na svoj racunar.
2. U korenu repozitorijuma pokreni:

```bash
python3 literatura/rehabilitacioni-protokoli/download.py
```

Skripta uzima adrese iz `sources.json`, proverava da je odgovor zaista PDF, racuna SHA-256 i cuva fajlove u `literatura/rehabilitacioni-protokoli/pdf/`. Taj folder je ignorisan od Git-a. Rezultati i neuspele adrese cuvaju se u `izvestaj-preuzimanja.json`.

**VALD i noviji Aspetar materijali** ostaju kao linkovi ka zvanicnim formularima - skripta ne pokusava da zaobidje registraciju. **Aspetar ACL smernice (2023)** mogu se citati u punom tekstu na PubMed Central preko linka gore; stari BJSM PDF link ponekad vraca 403, pa nije ukljucen u automatsko preuzimanje.

## Kako ovo ukljucujemo u MFS Masterklas

- Svaki original se vodi sa izdavacem, izdanjem ako je poznato, izvorom i statusom provere.
- Izdvojiti **klinicke indikacije, kontraindikacije, objektivne kriterijume prelaska u sledecu fazu, testove, vezbe i doziranje**, ali bez kopiranja citavih tekstova u nase lekcije.
- Za strucne lekcije koristiti originalne citate i povezati ih sa EX ID-jevima u [MFS Bazi vezbi](https://github.com/Nidza22/Mfs-baza-vezbi).
- Prioritet za obradu: **patelarna tendinopatija (Delaware), akutne povrede aduktora (Aspetar), zadnja loza (Aspetar), ACL (Delaware + Aspetar)**.
- Klasicni protokol nije zamena za individualnu procenu ili instrukcije hirurga. Neki dokumenti su stariji i zahtevaju proveru u novijoj literaturi.

## Prava autora

Linkovanje ne znaci da dokument ima dozvolu za javno repozitorijumsko redistribuiranje. Delaware na pojedinim dokumentima izricito dozvoljava reprodukciju **neizmenjenog** originala za klinicke, edukativne i istrazivacke svrhe; za ostale izvore uslovi moraju biti zasebno provereni. Zadrzati originalni izvor i autorstvo. Zadrzati kopije samo u obimu dozvoljenom uslovima izdavaca.

**Izvorna biblioteka:** [University of Delaware](https://sites.udel.edu/ptclinic/professionals/guidelines/) · [Nevada PT](https://www.nevpt.com/media-resources/protocols/) · [Aspetar](https://www.aspetar.com/en/professionals/aspetar-clinical-guidelines) · [VALD](https://resources.vald.com/practitioners-series)

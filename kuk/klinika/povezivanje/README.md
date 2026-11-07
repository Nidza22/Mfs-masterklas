# Kuk — kako Masterklas i Biblioteka vežbi rade zajedno

> **NOVI PRIORITET (7. novembar 2026):** ovaj pilot povezivanja je sačuvan kao edukativna beleška, ali za sada **ne nastavljamo povezivanje dijagnoza i vežbi**. Pre toga gradimo pouzdan pretraživač sa jedinstvenom kategorizacijom svih postojećih i budućih vežbi. [Kanon plana](https://github.com/Nidza22/Mfs-baza-vezbi/blob/main/docs/PLAN-PRETRAZIVAC-KATEGORIZACIJA-2026-11-07.md).

**Status:** planirani klinički most sa već napisanim edukativnim temama. Veze ka postojećim vežbama su **kandidati za stručnu proveru**, a ne gotovi rehabilitacioni protokoli.  
**Datum:** 7. novembar 2026.

## Pravilo sistema

**Prvo vežbu pravilno klasifikujemo, tek onda dokazujemo za koje ciljeve i stanja može biti primerena.**

[Kontrolisana kategorizacija u MFS Biblioteci vežbi](https://github.com/Nidza22/Mfs-baza-vezbi/blob/main/docs/kategorizacija-vezbi.md) · [Rečnik kategorija](https://github.com/Nidza22/Mfs-baza-vezbi/blob/main/data/exercise-taxonomy-v1.json) · [Početni indeks 68 vežbi](https://github.com/Nidza22/Mfs-baza-vezbi/blob/main/data/classification-index-v1.json).

Ovim **ne menjamo postojeće kliničke dijagnoze** niti tvrdimo da već imamo dovoljno vežbi za svaki problem. Klinička objašnjenja ostaju u Masterklasu, identitet i kategorizacija vežbi u Biblioteci; zasebne stručno proverene veze povezuju ova dva sloja.

## Logika jednog pretraživanja

1. **Osoba ima simptom.** Proveravaju se upozoravajući znaci i potreba za medicinskom procenom.
2. **Razmatra se više mogućih uzroka.** Bol na jednom mestu nije automatska dijagnoza.
3. **Biraju se relevantni testovi** i objašnjava šta pozitivan i negativan nalaz znače, uključujući ograničenja.
4. **Odredi se klinički cilj** (na primer tolerancija opterećenja odmicača kuka), a ne odmah naziv neke vežbe.
5. **Pretraži se Biblioteka po obrascu, regiji, mišićnoj funkciji i progresiji.**
6. **Za svaku vežbu proveri se poreklo i status tehnike.** Ako potreban tip vežbe ne postoji, dopunjava se nova porodica/varijanta uz stabilan identifikator.
7. **Tek posle stručne procene** razmatraju se specifična veza sa stanjem, kontraindikacije, doza i kriterijumi napredovanja. Svi individualni podaci ostaju van GitHub repozitorijuma.

## Prve četiri kliničke teme koje smo već napisali

| Tema | Šta imamo | Šta još nije potvrđeno |
|---|---|---|
| [Spoljašnji bol kuka / glutealne tetive](lateralni-bol-kuka.md) | Simptomi, testovi, literatura, primeri postojećih EX vežbi kao kandidata | Nedostaje zasebna, potvrđena porodica za odvođenje kuka; EX veze nisu odobren protokol |
| [Bol povezan sa aduktorima](aduktorski-bol-prepone.md) | Kriterijumi kliničke klasifikacije, palpacija i otpor, principi opterećenja | Nedostaje sistematska porodica za adukciju; nijedna vežba nije automatski dodeljena |
| [Proksimalna zadnja loža](proksimalna-zadnja-loza.md) | Lokalni simptomi, testovi i mogući zadaci iz baze | Opterećenje tetive, opseg savijanja kuka i tolerancija moraju se individualno proceniti |
| [Duboki prednji bol kuka](duboki-prednji-bol-kuka.md) | Diferencijalno razmatranje i indikacije za dalje testiranje/upуćivanje | Namerno **nema automatske veze ka terapijskoj vežbi** dok uzrok nije dovoljno razjašnjen |

## Šta nedostaje u Biblioteci?

Ovo nisu gotove vežbe ni novi identifikatori, nego **grupe za plansko proširenje**:

- Odvođenje kuka: početne izometrije, pokreti sa opremom, progresivno doziranje.
- Primicanje kuka: izometrija, dinamički otpor, kraća/duža poluga, sportski zadaci.
- Pregibači kuka: kontrolisani izometrijski i dinamički otpor.
- Zadnja loža: ciljana progresivna fleksija kolena i rad u različitim uglovima kuka.
- Rotacije kuka: jasno razdvojeni spoljašnji i unutrašnji rotacioni zadaci.

Kada dođemo do stanja za koje nedostaje kvalitetna porodica, prvo tražimo stručne demonstracije, dodajemo tehnički proverene opise, varijante i izvore, zatim razmatramo kliničku indikaciju. To je osnova budućeg proširivanja na druge zglobove.

## Šta ne sme da radi automatika?

- Ne birati vežbe samo po jednom pozitivnom testu.
- Ne dodeljivati fazu rehabilitacije samo prema težini vežbe.
- Ne zaključivati da vežba direktno leči tetivu zato što aktivira susedni mišić.
- Ne prikazivati preliminarnu oznaku kao stručno odobrenu vezu.
- Ne upisivati stvarne podatke o pacijentima u repozitorijum.

**Dalji praktični cilj:** dosledna klasifikacija svih vežbi, njihove porodice i provereni opisi → kvalitetna pretraga → ciljano proširenje baze prema Masterklasu.

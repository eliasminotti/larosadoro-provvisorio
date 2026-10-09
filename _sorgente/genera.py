#!/usr/bin/env python3
"""Genera le pagine del sito di Orizzonti Celesti.

Ogni pagina = intestazione comune + corpo (in _sorgente/pagine/) + piè di pagina comune.
Uso:
    python3 _sorgente/genera.py            -> pagine del sito, nella cartella principale
    python3 _sorgente/genera.py --prova    -> come sopra, con la nota «versione di lavoro»
"""
import pathlib
import sys

RADICE = pathlib.Path(__file__).resolve().parent.parent
PAGINE = RADICE / "_sorgente" / "pagine"

SITO = "https://orizzonticelesti.org"

# nome file, voce di menu, titolo della scheda, descrizione
MAPPA = [
    ("index.html", "Home", "Orizzonti Celesti",
     "Associazione svizzera di pubblica utilità: agricoltura biodinamica, formazione, cura delle persone, arte e ricerca, con radici nell'antroposofia."),
    ("chi-siamo.html", "Chi siamo", "Chi siamo · Orizzonti Celesti",
     "Storia, principi e organizzazione dell'Associazione Orizzonti Celesti di Bellinzona."),
    ("cosa-facciamo.html", "Cosa facciamo", "Cosa facciamo · Orizzonti Celesti",
     "Le attività in corso dell'Associazione Orizzonti Celesti, ambito per ambito."),
    ("visione.html", "Visione", "Visione · Orizzonti Celesti",
     "Il manifesto di Orizzonti Celesti: l'ecosistema sociale che l'associazione vuole far crescere."),
    ("sostienici.html", "Sostienici", "Sostienici · Orizzonti Celesti",
     "Tesseramento, donazioni, lasciti e collaborazione con l'Associazione Orizzonti Celesti."),
    ("contatti.html", "Contatti", "Contatti · Orizzonti Celesti",
     "Contatti e dati legali dell'Associazione Orizzonti Celesti, Bellinzona."),
]

TESTA = """<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{titolo}</title>
<meta name="description" content="{descrizione}">
<link rel="canonical" href="{sito}/{percorso}">
<meta property="og:type" content="website">
<meta property="og:locale" content="it_CH">
<meta property="og:site_name" content="Orizzonti Celesti">
<meta property="og:title" content="{titolo}">
<meta property="og:description" content="{descrizione}">
<meta property="og:url" content="{sito}/{percorso}">
<link rel="icon" href="img/simbolo.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Alegreya+Sans:ital,wght@0,400;0,500;0,700;1,400&family=Marcellus&display=swap">
<link rel="stylesheet" href="css/stile.css">
</head>
<body>
<header class="testata">
  <div class="contenitore">
    <a class="marchio" href="./">
      <img src="img/simbolo.svg" alt="" width="48" height="48">
      <span><strong>Orizzonti Celesti</strong><small>Associazione</small></span>
    </a>
    <nav class="menu" aria-label="Menu principale">
      <ul>
{menu}
      </ul>
    </nav>
  </div>
</header>
{nota}<main>
"""

NOTA = """<div class="nota-lavoro" role="note">
  <div class="contenitore">Versione di lavoro: struttura e contenuti. La grafica si sceglie dopo, fra i prototipi. I riquadri tratteggiati sono le parti da completare.</div>
</div>
"""

PIEDE = """</main>
<footer class="piede">
  <div class="contenitore">
    <div>
      <h2>Associazione Orizzonti Celesti</h2>
      <p>Associazione di pubblica utilità senza scopo di lucro, ai sensi degli articoli 60 e seguenti del Codice civile svizzero.</p>
    </div>
    <div>
      <h2>Sede</h2>
      <p>c/o Elias Minotti<br>Via Mezzavilla 12<br>6503 Bellinzona, Svizzera</p>
    </div>
    <div>
      <h2>Dati dell'ente</h2>
      <p>IDI CHE-143.778.999<br>Registro di commercio del Cantone Ticino, CH-501.6.015.557-6<br>associazione@orizzonticelesti.org</p>
    </div>
  </div>
</footer>
</body>
</html>
"""


def menu(corrente):
    righe = []
    for nome, voce, _, _ in MAPPA:
        href = "./" if nome == "index.html" else nome
        attuale = ' aria-current="page"' if nome == corrente else ""
        righe.append(f'        <li><a href="{href}"{attuale}>{voce}</a></li>')
    return "\n".join(righe)


def genera(prova=False):
    for nome, _, titolo, descrizione in MAPPA:
        corpo = (PAGINE / nome).read_text(encoding="utf-8")
        percorso = "" if nome == "index.html" else nome
        html = TESTA.format(
            titolo=titolo,
            descrizione=descrizione,
            sito=SITO,
            percorso=percorso,
            menu=menu(nome),
            nota=NOTA if prova else "",
        ) + corpo.rstrip() + "\n" + PIEDE
        (RADICE / nome).write_text(html, encoding="utf-8")
        print("scritta", nome)


if __name__ == "__main__":
    genera(prova="--prova" in sys.argv)

# Methoden und Werkzeuge

## Methodenwahl

Wähle nach Erkenntnisbedarf, nicht nach maximaler Methodenzahl. Nutze einen schlanken Kern aus Rahmung, Evidenzprüfung, Dynamikprüfung, Alternativen und Gegenprüfung. Die Tabellen und Regeln unten sind eine auf diesen Skill zugeschnittene Operationalisierung; sie sind kein validiertes Messinstrument.

| Bedarf | Technik | Konkretes Ergebnis | Grenze |
|---|---|---|---|
| Neue Entwicklungen finden | Horizon Scanning, STEEP/PESTEL als Suchraster | belegte Signale mit Relevanz und Gegenkräften | Sichtbarkeit ist nicht Bedeutung; schwaches Signal ist kein Trendbeweis |
| Gewissheit und Offenheit trennen | Ankerprüfung, Annahmenregister, Wirkungs-/Unsicherheitsmatrix | gemeinsames Fundament und kritische Variablen | Einschätzung mit Begründung statt objektiv erscheinender Scores |
| Nichtlinearität verstehen | Zeitreihen- und Mechanismenprüfung | mögliche Dynamiken, Grenzen und Sensitivitäten | Datenfit beweist keinen Mechanismus oder Zukunftspfad |
| Rückwirkungen erkennen | Wirkungsnetz, Kausalschleifen, Futures Wheel | direkte und indirekte Folgen samt Verzögerungen | Pfeile sind Kausalhypothesen, keine Belege |
| Unterschiedliche Zukünfte bilden | morphologische Analyse, bei Eignung 2×2-Matrix | konsistente Kombinationen kritischer Ausprägungen | keine Scheingenauigkeit oder künstliche Unabhängigkeit |
| Widersprüche finden | qualitative Cross-Impact-/Konsistenzprüfung | nachvollziehbare Vereinbarkeitsprüfung | keine formale Cross-Impact-Balance behaupten ohne deren tatsächliche Durchführung |
| Eigene Denkfehler erkennen | Gegenhypothesen, Perspektivwechsel, strukturierte Gegenprüfung | stärkster Einwand, offene Brücke, alternative Erklärung | KI-Rollen sind keine unabhängigen Fachpersonen |
| Entscheidungen unterstützen | Wind-Tunnelling, Backcasting, reversible Experimente | robuste Optionen und bedingte Schritte | normative Zielwahl offenlegen; kein zukünftiger Erfolg garantiert |
| Später neu bewerten | Frühindikatoren und Annahmenmonitoring | beobachtbarer Auslöser für Revision | mehrere Indikatoren triangulieren, keine automatische Überwachung vortäuschen |

## Entwicklungsverläufe sauber prüfen

1. Definiere Variable, Einheit, Bezugsgruppe, Region, Zeitraum und Messmethode. Kläre, ob der Wert ein Bestand, Fluss, Preis, Anteil, Index oder Benchmark ist.
2. Prüfe Vergleichbarkeit, fehlende Werte, Nennerwechsel, Stichprobenwechsel, nominale/reale Preise, Versionswechsel und Ober-/Untergrenzen. Werte fehlende Beobachtungen nicht als null.
3. Stelle bei Bedarf dieselben Daten auf linearer und logarithmischer Skala dar. Logarithmen nur für strikt positive Werte; keinen künstlichen Offset ohne sachliche Begründung einführen.
4. Vergleiche absolute Änderung pro Zeiteinheit und relative Rate. Nutze bei ungleichen Intervallen zeitnormierte Raten. Eine Endpunkt-CAGR verbirgt Zwischenverläufe.
5. Untersuche Mechanismen und externe Bedingungen. Variiere Beobachtungsfenster, Ausreisserbehandlung und Annahmen; benenne fehlende Identifizierbarkeit.
6. Verwende Fits nur bei ausreichenden Daten. Vergleiche Fehler auf derselben Skala; prüfe Residuen, Parameterstabilität und, wenn tragfähig, zeitlich zurückgehaltene Daten. Wähle nicht allein nach R². Ein kurzer Ausschnitt identifiziert weder Exponentialität noch Sättigungsniveau zuverlässig.
7. Leite mögliche Fortsetzungen bedingt ab. Eine Fortsetzung, eine begründete Bremsung und ein begründeter Strukturbruch können hilfreich sein; erzwinge diese drei nicht ohne Mechanismus.

| Form | Kennzeichen | Nötige Vorsicht |
|---|---|---|
| Linear: y=a+bt | annähernd gleiche absolute Änderungen pro Zeit | abnehmende relative Rate bei positivem b ist kein Beweis einer absoluten Verlangsamung |
| Exponentiell: y=a·exp(kt) | konstante relative Rate; bei k>0 zunehmende absolute Zuwächse | Verdopplungszeit ln(2)/k nur bei konstantem k>0; nicht auf unbegrenzte Zeit extrapolieren |
| Veränderliche relative Rate | k(t) steigt oder fällt | exponentielles Wachstum ist nicht gleich steigende prozentuale Rate; Datenrauschen prüfen |
| Potenzfunktion | Skalierung mit Potenz einer definierten Bezugsgrösse | Zeitursprung bzw. zugrunde liegende Grösse offenlegen; nicht mit Exponentialfunktion verwechseln |
| Sättigung / S-Kurve | frühes Wachstum, später kleinerer Zuwachs | obere Grenze und Wendepunkt nicht aus wenigen frühen Punkten erfinden |
| Schwelle / Regimewechsel | Änderung bei veränderten Bedingungen | Auslöser und neue Regeln benennen; Sprung nicht nachträglich zur Dauerwachstumsrate erklären |
| Zyklus / gemischter Verlauf | wiederkehrende oder überlagerte Bewegungen | Konjunktur, Saisonalität und strukturellen Trend auseinanderhalten |

Beschleunigung immer relativ zur Messgrösse erklären. Sinkende Rechenkosten können beispielsweise die Verfügbarkeit erhöhen, ohne dass Lernzuwächse, Einführung oder Beschäftigungswirkungen dieselbe Kurvenform haben. Zwischenstufen separat belegen.

### Deskriptives Rechenwerkzeug

Führe bei geeigneten Daten aus:

```bash
python scripts/trend_diagnostics.py daten.csv --time-unit Jahre --value-unit 'Indexpunkte'
```

Verwende eine CSV mit `time,value`, Dezimalpunkt und konsistenter Zeiteinheit, etwa Dezimaljahre. Das Skript sortiert Zeitpunkte, verwirft doppelte/nichtendliche/leere Werte und benötigt mindestens zwei Beobachtungen. Es gibt JSON auf stdout aus: Intervalllängen, zeitnormierte absolute Änderungen, relative Änderungen und bei durchgehend positiven Werten logarithmische/geometrische Raten. Bei nichtpositiven Werten unterbleibt die relative Wachstumsdiagnostik. Es prognostiziert nicht, testet keine statistische Signifikanz und klassifiziert keine Kurve. Prüfe Datenbedeutung und Unsicherheit selbst. Zwei Punkte erlauben Veränderung, keine Beschleunigungsdiagnose.

## Wirkungsnetz und Folgen

Beginne mit einer für die Leitfrage relevanten Änderung. Erfasse direkte Folgen, daraus entstehende zweite Folgen und Rückwirkungen. Notiere an jeder Verbindung: Beleg oder Hypothese, verstärkende/dämpfende Wirkung, Verzögerung und Geltungsbedingung. Vermeide die Doppelzählung derselben Wirkung über mehrere Pfade.

Prüfe Gegenreaktionen von Lernenden, Lehrenden, Unternehmen, Institutionen und Politik. Ergänze Ressourcen, Verteilung, Marktmacht, Anreize und kulturelle Akzeptanz. Stelle nur die entscheidenden Verbindungen grafisch dar; eine lange Pfeilkette ist keine kausale Begründung.

## Szenarioraum und Konsistenz

1. Wähle zur Leitfrage wenige wirksame Unsicherheiten. Behandle harte Anker nicht als variable Achsen.
2. Formuliere für jede Dimension unterscheidbare, begründbare Ausprägungen. Beispielhafte Dimensionen ohne Faktstatus: Zugang zu lernwirksamer KI, institutionelle Anerkennung neuer Kompetenznachweise, Verfügbarkeit betrieblicher Lernzeit.
3. Kombiniere Ausprägungen. Markiere Paare als vereinbar, bedingt vereinbar oder widersprüchlich; begründe Bedingungen und halte Unwissen offen. Nutze nicht mechanisch alle Kombinationen.
4. Prüfe danach das Gesamtbild: Paarweise Vereinbarkeit garantiert noch keine globale Konsistenz. Prüfe Zeithorizont, Ressourcen und gegenseitige Voraussetzungen gemeinsam.
5. Wähle drei bis vier logisch unterschiedliche Szenarien mit erkennbarem Nutzen für die Leitfrage. Kennzeichne Lücken im abgedeckten Raum.
6. Führe jedes Zukunftsbild auf Ausgangspunkt, kritische Übergänge und Voraussetzungen zurück. Erfinde keine präzisen Ereignisdaten, wenn nur bedingte Phasen tragfähig sind.

Führe eine 2×2-Matrix nur ein, wenn beide Achsen ausreichend eigenständig sind. «KI-Fähigkeit» und «KI-Verbreitung» können zusammenhängen; begründe eine getrennte Variation oder wähle eine mehrdimensionale Struktur. Erkläre Abhängigkeiten statt sie zu verschweigen.

## Gegenprüfung und Erweiterung

Prüfe die stärkste Gegenposition, nicht einen leicht widerlegbaren Strohmann. Untersuche Bestätigungsfehler, Technikzentrierung, institutionellen Status-quo-Bias, westliche/wohlhabende Perspektive und erwünschte Ergebnisse. Ein heutiger Engpass kann lösbar sein; ein technischer Fortschritt kann an unveränderten Anreizen scheitern.

Verwende einen methodisch begründeten Stressfall bei relevantem Bedarf. Bezeichne ein konkretes Ereignis nicht ohne Beleg als «unwahrscheinlich» mit Zahlen. Behandle neuartige wissenschaftliche Hypothesen als solche, nicht als Science-Fiction und nicht als erwiesene Zukunft.

Nutze Delphi nur bei tatsächlicher strukturierter Befragung mehrerer realer Fachpersonen. KI-simulierte Rollen können Fragen erzeugen, aber keine empirische Expertenübereinstimmung begründen. Interviews oder Einladungen nur bei ausdrücklichem Auftrag tatsächlich durchführen.

## Entscheidungen und Frühindikatoren

Teste eine Option gegen alle Szenarien: Nutzen, Nebenwirkungen, Ressourcen, Abhängigkeiten, Reversibilität und Belastungen für unterschiedliche Gruppen. Wähle keine Option allein deshalb, weil sie zu einem bevorzugten Zukunftsbild passt.

Verwende Backcasting bei ausdrücklich gewünschtem Zielzustand: Welche vorherigen Bedingungen wären erforderlich, welche sind steuerbar, welche extern? Bezeichne diese Rückwärtsplanung als normativ.

Formuliere Indikatoren als Messplan: Definition, Datenquelle, Beobachtungsrhythmus, begründete Schwelle oder qualitative Signalkombination und Revisionsentscheidung. Prüfe auch Gegenindikatoren. Plane keine Hintergrundrecherche als bereits laufend, wenn kein entsprechender Dienst eingerichtet ist.

## Technische Ausstattung

- **Erforderlich für aktuelle Faktenprüfung:** Web-/Literatursuche mit Zugriff auf Originalquellen sowie PDF-/Dokumentenlesen; ohne Zugriff ausdrücklich eingeschränkte Prüfung.
- **Bei Zahlen erforderlich:** Python oder Tabellenkalkulation, Einheitenprüfung und nachvollziehbare Rechenschritte; das mitgelieferte Skript genügt für einfache Veränderungen.
- **Für komplexere Modelle optional:** Zeitreihenanalyse, Wirkungsnetz oder System-Dynamics-Modell; nur mit expliziten Annahmen, dokumentierter Kalibrierung und Sensitivität.
- **Für längere Vorhaben sinnvoll:** versioniertes Quellen-/Annahmenregister und exportierbare Tabellen. Vorhandene Dateien aktualisieren, Quellenstand erhalten.
- **Kein Pflichtkauf:** Nutze verfügbare Werkzeuge. Verkaufe Literaturverwaltung, Datenbankzugänge oder Spezialsoftware nicht als Voraussetzung für seriöse qualitative Szenarien.

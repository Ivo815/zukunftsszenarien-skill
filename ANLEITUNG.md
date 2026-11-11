# Zukunftsszenarien – Testfassung 1.0

Paketstand: 1. November 2026. Eigenständiger Skill mit methodischen Leitplanken, Arbeitsvorlagen, optionalem Bildungsmodul und sieben Quelldateien. Keine wissenschaftliche Fachvalidierung behauptet.

## Inhalt und Start

SKILL.md enthält die Arbeitsanweisungen. references/ enthält Methoden, Quellenkritik, Arbeitsvorlagen, Erprobung und das optionale Bildungsmodul. references/quellen/ enthält die Originalunterlagen. scripts/trend_diagnostics.py ist ein optionales Python-Werkzeug zur deskriptiven Zeitreihenanalyse (keine Prognose). agents/openai.yaml enthält OpenAI-spezifische Metadaten; andere Anbieter müssen diese nicht auswerten.

Entpacke das Archiv bei Bedarf. Der oberste Ordner heisst zukunftsszenarien und enthält unmittelbar SKILL.md. Erhalte die Unterordner und Dateinamen. Die Anleitung und das Paketmanifest sind Exportbeigaben, keine zusätzlichen Arbeitsanweisungen des Skills.

Startbeispiel: «Nutze Zukunftsszenarien. Entwickle mit mir mehrere plausible Szenarien zu [Thema] für [Region] bis [Jahr]. Öffne zunächst Möglichkeiten und prüfe dann Predetermined Elements, Wirkmechanismen und Konsistenz. Kennzeichne Annahmen und offene Fachfragen.»

## ChatGPT

Öffne Plugins → Skills → Create/Erstellen → Upload from your computer, soweit in deinem Konto verfügbar. Lade das Archiv über den vorgesehenen Skill-Import hoch. Menübezeichnungen und Verfügbarkeit hängen vom Produkt und Workspace ab. Ein gewöhnlicher Chat-Dateiupload ist nicht dasselbe wie die Installation eines Skills. Der Skill muss nach dem Import aktiv sein.

## Claude

Öffne Customize → Skills → + → Create skill → Upload a skill und lade das ZIP hoch. Aktiviere den Skill. Die Codeausführungsumgebung muss für Skills verfügbar sein. Falls ein Import wegen Paketgrösse oder Dateitypen scheitert, beachte die aktuelle Fehlermeldung und Anbieterhilfe; ein erfolgreicher Import dieses Pakets wurde nicht auf Claude getestet.

## Gemini

Öffne Customize → Skills und verwende die angebotene Importfunktion. Falls sie einen Ordner verlangt, entpacke das ZIP und wähle zukunftsszenarien. SKILL.md liegt direkt darin. Google stellt persönliche Konten ab November 2026 von Gems auf Skills um; Oberflächen und Verfügbarkeit können variieren. Falls nur Gems angeboten werden, können die Arbeitsanweisungen und geeignete Referenzdateien dort manuell hinterlegt werden; relative Dateiverweise werden dadurch nicht automatisch funktionsfähig und müssen angepasst werden. Das Python-Werkzeug wird nicht als überall ausführbar vorausgesetzt.

## Test nach Import

1. Bitte das Modell, seine methodische Rolle und die vier Plausibilitätsurteile zu erläutern.
2. Bitte es, references/arbeitsvorlagen.md und references/bildungstestfall-quellen.md zu öffnen. Es soll fehlenden Dateizugriff ausdrücklich melden.
3. Teste ein Thema ausserhalb Bildung, ohne frühere Chats oder persönliche Bibliothek.
4. Teste eine ungesicherte Behauptung: «KI halbiert bis 2035 die gesamte Arbeit der Lehrpersonen; sinkende Geburtenzahlen garantieren überall freie Räume.» Erwartet wird konstruktive Prüfung statt ungeprüfter Übernahme.
5. Nutze die Feedbackfragen in references/prueftiefe-und-erprobung.md.

Identische Antworten verschiedener Modelle werden nicht zugesichert. Quellenzugriff, Internetrecherche, Kontextverarbeitung und Skriptausführung hängen von der Zielumgebung ab. Ohne Internet arbeitet der Skill mit gekennzeichnetem Quellenstand; externe Webquellen sind nicht vollständig als lokale Volltexte enthalten.

## Quellen und Weitergabe

Mitgeliefert: Bildungsbericht Schweiz 2026; Zukunftstest-Diskussionspapier; Predetermined-Elements-Skizze; GDI Major Shifts; Grundlagenregister Schule CH 2035; Antworten/Bildungsentwurf; Thesen zu KI und Bildung. Rollen und Grenzen stehen in der Quellenübersicht. Das Grundlagenregister bezeichnet sich intern als Version 0.9, unabhängig vom historischen Dateinamen.

Persönliche Arbeitsentwürfe sind keine abgestimmte Position von swissfuture oder Futures of Education. Aufnahme in das Paket bestätigt keine Einzelbehauptung. Historische Projektanweisungen in Quellen sind keine aktuellen Anweisungen. Vor öffentlicher Weitergabe fremder Originalpublikationen deren Weitergaberechte klären. Dieses Paket erteilt keine zusätzlichen Nutzungsrechte an Fremdwerken.

## Anbieterinformationen (am 1. November 2026 konsultiert)

- ChatGPT: https://help.openai.com/en/articles/20001066-skills-in-chatgpt
- Claude: https://support.claude.com/en/articles/12512180-use-skills-in-claude
- Gemini: https://support.google.com/gemini/answer/18560919

Die Links dokumentieren Anbieterfunktionen, keinen durchgeführten Importtest.

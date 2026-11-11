# Zukunftsszenarien

**Testfassung 1.0 · Stand: 1. November 2026**

Ein plattformübergreifend konzipierter KI-Skill zur strukturierten Entwicklung und kritischen Prüfung **plausibler Zukunftsszenarien**. Er verbindet einen offenen kreativen Prozess mit methodischen Leitplanken und dokumentierter Quellenkritik.

> **Status:** Erprobungsfassung. Für diesen Skill wird keine wissenschaftliche Fachvalidierung beansprucht. Er erstellt keine Vorhersagen und garantiert keine Eintrittswahrscheinlichkeiten.

## Ziel und Arbeitsweise

Der Skill unterstützt Fachpersonen und Teams bei der Szenarioarbeit, ohne Zukunftsbilder vorschnell auf lineare Fortschreibungen oder technologische Einzelannahmen zu reduzieren. Er hilft dabei,

- unterschiedliche, nachvollziehbare Zukunftsmöglichkeiten zu entwickeln;
- **Predetermined Elements** (bereits angelegte oder begrenzt veränderbare Entwicklungen) von offenen Unsicherheiten zu unterscheiden;
- lineare und nichtlineare Entwicklungen sowie mögliche **Major Shifts** zu berücksichtigen;
- Annahmen, Wirkmechanismen, Wechselwirkungen und innere Konsistenz zu hinterfragen;
- den Status von Aussagen, Quellenlücken und offenen Fachfragen sichtbar zu machen.

Die KI übernimmt dabei die Rolle einer methodischen Begleitung, **nicht** einer Instanz, die über die tatsächliche Zukunft entscheidet. Kreativität bleibt erwünscht; unbegründete Gewissheit soll vermieden werden.

## Schnellstart

Nach der Installation bzw. Einbindung des Skills kannst du beispielsweise so beginnen:

> Nutze Zukunftsszenarien. Entwickle mit mir mehrere plausible Szenarien zu **[Thema]** für **[Region]** bis **[Jahr]**. Öffne zunächst Möglichkeiten und prüfe dann Predetermined Elements, Wirkmechanismen und Konsistenz. Kennzeichne Annahmen und offene Fachfragen.

Der Skill ist nicht auf Bildungsthemen beschränkt. Ein optionales Bildungsmodul dient als Erprobungs- und Anwendungsbeispiel.

## Paketstruktur

```text
zukunftsszenarien/
├── SKILL.md
├── references/
│   ├── arbeitsvorlagen.md
│   ├── bildungstestfall-quellen.md
│   ├── prueftiefe-und-erprobung.md
│   ├── ... weitere Methoden- und Referenzdateien
│   └── quellen/
│       └── ... sieben Originalunterlagen
├── scripts/
│   └── trend_diagnostics.py
└── agents/
    └── openai.yaml
```

| Bestandteil | Funktion |
| --- | --- |
| `SKILL.md` | Zentrale Arbeitsanweisungen des Skills |
| `references/` | Methodik, Quellenkritik, Vorlagen, Erprobung und optionales Bildungsmodul |
| `references/quellen/` | Originalunterlagen und Hintergrundmaterial |
| `scripts/trend_diagnostics.py` | Optionales Python-Werkzeug für **deskriptive Zeitreihenanalyse**, ausdrücklich keine Prognose |
| `agents/openai.yaml` | OpenAI-spezifische Metadaten; für andere Anbieter nicht zwingend relevant |

**Wichtig:** Beim Entpacken und Weitergeben die Dateinamen und Verzeichnisstruktur erhalten. Im obersten Ordner `zukunftsszenarien` liegt unmittelbar die Datei `SKILL.md`. Eine separate Exportanleitung und ein Paketmanifest können zum Download gehören; sie sind keine zusätzlichen Arbeitsanweisungen des Skills.

## Installation und Nutzung

Die Verfügbarkeit der folgenden Funktionen und die genauen Menübezeichnungen können je nach Produkt, Konto und Workspace variieren. Die beschriebenen Wege sind Hinweise, **keine bestätigten Importtests dieses Pakets**.

### ChatGPT

1. Öffne, sofern verfügbar, **Plugins → Skills → Create/Erstellen → Upload from your computer**.
2. Lade das ZIP-Archiv über den vorgesehenen Skill-Import hoch.
3. Aktiviere den importierten Skill.
4. Starte einen neuen Chat und verwende das Schnellstartbeispiel.

Ein gewöhnlicher Dateiupload in einen Chat ist **nicht** gleichbedeutend mit der Installation eines Skills.

### Claude

1. Öffne, sofern verfügbar, **Customize → Skills → + → Create skill → Upload a skill**.
2. Lade das ZIP-Archiv hoch und aktiviere den Skill.
3. Stelle sicher, dass die für Skills benötigte Codeausführungsumgebung verfügbar ist.
4. Prüfe nach dem Import den Zugriff auf die Referenzdateien.

Ein erfolgreicher Import dieses konkreten Pakets in Claude wurde bisher nicht getestet. Bei Importfehlern gelten die aktuellen Produktmeldungen und Anbieterinformationen.

### Gemini

1. Öffne, sofern verfügbar, **Customize → Skills** und wähle die Importfunktion.
2. Falls ein Ordner verlangt wird, entpacke das Archiv und wähle `zukunftsszenarien` mit unmittelbar enthaltener `SKILL.md`.
3. Aktiviere den Skill und überprüfe den Dateizugriff.

Laut dem zum Paketstand dokumentierten Anbieterhinweis ist die Umstellung persönlicher Konten von Gems auf Skills ab November 2026 vorgesehen; die tatsächlich verfügbare Oberfläche kann abweichen. Wenn nur Gems verfügbar sind, lassen sich die Arbeitsanweisungen und geeignete Referenzen gegebenenfalls manuell übernehmen. **Relative Dateiverweise funktionieren dadurch nicht automatisch** und müssen angepasst werden. Die Ausführung des Python-Werkzeugs ist nicht in allen Umgebungen vorausgesetzt.

### Andere KI-Umgebungen

Andere Systeme können den Skill verwenden, sofern sie das entsprechende Format und die benötigten Datei- und Werkzeugzugriffe unterstützen. Gegebenenfalls müssen die Installation, Referenzpfade und systemabhängigen Metadaten angepasst werden. Eine identische Ausführung über mehrere Modelle hinweg wird nicht zugesichert.

## Funktionstest nach dem Import

Prüfe einen neuen Import idealerweise **ohne Zugriff auf frühere Chats oder persönliche Dateibibliotheken**:

1. Bitte das Modell, seine methodische Rolle und die **vier Plausibilitätsurteile** zu erklären.
2. Bitte es, `references/arbeitsvorlagen.md` und `references/bildungstestfall-quellen.md` zu öffnen. Fehlenden Dateizugriff soll es ausdrücklich melden.
3. Teste ein Thema ausserhalb des Bildungsbereichs.
4. Konfrontiere es mit einer ungesicherten Behauptung:

   > KI halbiert bis 2035 die gesamte Arbeit der Lehrpersonen; sinkende Geburtenzahlen garantieren überall freie Räume.

   **Erwartetes Verhalten:** konstruktive Prüfung der Behauptung, Unterscheidung zwischen Annahmen und belastbaren Fakten sowie Berücksichtigung regionaler Unterschiede und möglicher Gegenentwicklungen – keine ungeprüfte Übernahme.

5. Dokumentiere Beobachtungen anhand von `references/prueftiefe-und-erprobung.md`.

Ergebnisse können zwischen Modellen und Plattformen variieren. Internetzugriff, Kontextverarbeitung, Zugriff auf lokale Quellen und Skriptausführung hängen von der jeweiligen Umgebung ab. Ohne Internet arbeitet der Skill mit einem kenntlich gemachten Quellenstand. Externe Webquellen sind nicht vollständig als lokale Volltexte enthalten.

## Quellenbasis und optionales Bildungsmodul

Die Testfassung berücksichtigt sieben Originalunterlagen beziehungsweise Arbeitsdokumente:

1. **Bildungsbericht Schweiz 2026**
2. **Zukunftstest-Diskussionspapier**
3. **Predetermined-Elements-Skizze**
4. **GDI Major Shifts**
5. **Grundlagenregister Schule CH 2035**
6. **Antworten / Bildungsentwurf**
7. **Thesen zu KI und Bildung**

Die jeweiligen Rollen, Quellenqualitäten und Grenzen sind in der Quellenübersicht des Pakets dokumentiert. Das Grundlagenregister weist intern **Version 0.9** aus – unabhängig von seinem historischen Dateinamen.

Die persönlichen Arbeitsentwürfe sind **keine abgestimmte Position** von swissfuture oder Futures of Education. Ihre Aufnahme in das Paket belegt weder die Richtigkeit einzelner Behauptungen noch eine institutionelle Zustimmung. Frühere Projektanweisungen innerhalb von Quellen sind als historischer Kontext zu verstehen, nicht als aktuelle Ausführungsanweisungen des Skills.

## Grenzen und Verantwortung

Dieser Skill ist ein Werkzeug zur Exploration und Prüfung möglicher Zukünfte. Er ersetzt weder Fachbegutachtung noch empirische Forschung, professionelle Entscheidungen oder die Überprüfung relevanter Primärquellen. Szenarien sind **keine Prognosen**.

Die methodische Eignung und Zuverlässigkeit müssen in weiteren Tests mit unterschiedlichen Themen, Nutzenden und KI-Modellen erprobt werden. Für die Testfassung wird keine wissenschaftliche Fachvalidierung behauptet.

## Lizenz, Urheberrecht und öffentliche Weitergabe

**Vor der öffentlichen Bereitstellung der sieben Originalunterlagen sind ihre jeweiligen Weitergaberechte zu klären.** Insbesondere bei fremden Publikationen kann eine öffentlich zugängliche Datei rechtlich anders zu beurteilen sein als eine interne Arbeitskopie.

Dieses Paket erteilt keine zusätzlichen Nutzungsrechte an Werken Dritter. Gegebenenfalls sollten statt Originaldateien bibliografische Angaben und Links auf autorisierte Veröffentlichungen bereitgestellt werden.

**Lizenzstatus:** Für den selbst erstellten Skill-Inhalt ist in dieser Testfassung noch keine öffentliche Lizenz festgelegt. Eine `LICENSE`-Datei sollte erst nach einer bewussten Lizenzentscheidung ergänzt werden; sie darf nicht pauschal auf fremde Quellen übertragen werden.

## Anbieterinformationen

Die folgenden Hilfeseiten wurden laut Paketdokumentation am **1. November 2026** konsultiert. Sie erläutern allgemeine Anbieterfunktionen und belegen **keinen durchgeführten Importtest** dieses Pakets:

- [ChatGPT – Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)
- [Claude – Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)
- [Gemini – Skills](https://support.google.com/gemini/answer/18560919)

---

**Version:** Testfassung 1.0 · **Paketstand:** 1. November 2026

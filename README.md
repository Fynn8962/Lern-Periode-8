

Fynn Huber
10.01.2025

# Mein Projekt
Mein Projekt ist ein einfaches Python Tic-Tac-Toe Spiel gegen einen Randomized "Bot". Man kann das Feld  mittels drücken der Zahl auf der Tastatur auswählen, auf welches man Setzen will. Gewinnt man eine Runde, bekommt man einen Punkt. Wer zuerst Drei Punkte hat, gewinnt das Spiel. Durch überprüfung der Felder ist es nicht möglich Felder mehrmals zu wählen. Ist es unentschieden wird das Spiel einfach weitergeführt. 

**Gameplay:**
<img src="https://github.com/Fynn8962/Lern-Periode-8/blob/main/LP8-Gif-Python1.gif" alt="Gif Python Spiel" width="500" >

**Spielbrett:**
<img src="https://github.com/Fynn8962/Lern-Periode-8/blob/main/LP8-png-Python.png" alt="" width="500" >

&nbsp;
 
&nbsp;

## Grob-Planung
Da wir diese lern-Periode nur 4 Sitzungen Zeit haben ist dies gut um ein etwas kleines zu machen wie zum Beispiel eine neue Sprache oder neue Techniken auszuprobieren. Ich möchte eine kleine Konsolen-Applikation mit Python machen. Ich möchte etwas klassisches simples wie zum Beispiel ein Tic-Tac-Toe Game machen. 

&nbsp;
 
&nbsp;

### 10.01.2025

- [x] M295 das Video Tutorial (LA6402) beenden damit in mit den Aufträgen anfangen kann.
- [x] Mich mit Python vertraut machen; Syntax, IDE etc.
      
&nbsp;

**Heute habe ich**     
Zuerst habe ich im Modul 295 das Lernvideo auf LinkedIn fertig geschaut, da ich, das noch fertigmachen wollte, bevor ich zu lange warte und dann den Kontext vergessen habe. Im Lernvideo musste ging es um Rest-API, Endpoints etc. und ich musste das Beispielprojekt parallel mitcoden. Anschliessend habe ich mich mit den Basics von Python beschäftigt, wie der Syntax ist, von den Funktionen, wie man Sachen ausgibt und so weiter. Ich werde mein kleines Übungsprojekt wahrscheinlich in VS-Code erstellen.

&nbsp;
 
&nbsp;

### 17.01.2025

- [x] LB im Modul 450, Mock Klassen nach UML-Diagramm Implementieren
- [x] LB im Modul 450, Die Funktionalität meines Codes erweitern
- [x] LB im Moudl 450, UnitTest für die Klasse Benutzer schreiben
- [ ] LB im Modul 450, ein Codereview zu meinem Code schreiben. 
      
&nbsp;

**Heute habe ich**   
Heute habe ich an der LB im Modul 450 gearbeitet. Ich habe ein neues Projekt zum Testen erstellt und in diesem dann die Mock Klassen erstellt, die ich im UML-Diagramm definiert habe. Danach habe ich einen Unittest erstellt, um die Klasse Benutzer zu testen, mithilfe des Mocks, denn ich erstellt hatte. Anschliessend habe ich meine Dokumentation überarbeitet und detailliert beschrieben, was ich gemacht habe und wieso. Am Ende hatte ich die Logik meines Codes noch verändert, damit diese mehr Sinn macht und musste dies dann noch in meinem UML-Diagramm anpassen.
&nbsp;
 
&nbsp;

### 24.01.2025

- [x] Mit Python vertraut machen (Tutorials schauen, Projekt erstellen)
- [x] Anfangen mit meinem Tic-Tac-Toe Spiel, Projekt erstellen und Gedanken machen wie es aufgebaut sein soll.
- [x]  Spieloberfläche erstellen (Spielfeld, Eingabe, Ausgabe)
- [x]  Logik / Spielregeln von Tic-Tac-Toe Coden.
      
      
&nbsp;

**Heute habe ich**   
Ich habe mir zuerst ein Tutorial angeschaut über Python Grundlagen in welchem erklärt wurde, wie man ein Projekt erstellt und wie der grundlegende Syntax ist. Als ich vertraut war mit dem, was ich wissen wollte, fing ich an mit dem Spiel. Ich wusste anfangs nicht, wie ich das Spielfeld am besten umsetzen soll weshalb ich das gegoogelt habe. Nachdem ich das Spielfeld mittels eines dictionarys erstellt hatte, habe ich ohne Tutorial weitergemacht. Das, was mir am meisten Probleme machte, war der Syntax von Python und dass ich viele Schreibweisen nicht wusste (while, if-else, switchcase). Auch dass Python ohne geschwungene Klammern arbeitet, war anfangs ungewohnt und etwas verwirrend. Schlussendlich konnte ich aber das Spiel fertig coden. Der "Bot" gegen den man spielt, hat keine Logik, was es sehr einfach macht zu gewinnen. Den Code habe ich hochgeladen.
&nbsp;
 
&nbsp;

### 31.01.2025

- [ ] Zweiter Spielmodus, damit Spieler gegen Spieler gespielt werden kann. 
- [x] Möglichkeit mehrmals zu spielen einbauen (evt. Punkteanzeige)
- [x] Fehler beheben, z. B. Was passiert, wenn es keinen Gewinner gibt.
      
      
&nbsp;

**Heute habe ich**   
Ich habe in meinem Python-Tic-Tac-Toe-Game hinzugefügt, dass man mehrere Runden spielen kann, bis der Spieler oder der Computer 3 Punkte hat. Die Umsetzung ging sehr schnell, da ich einfach eine While-Schleife erstellt habe, welche die Punkte überprüft. Jedes Mal, wenn ein Punkt erzielt wird, erhöht sich die Punktzahl des Spielers oder des Computers um eins. Danach habe ich gemerkt, dass es ja auch Unentschieden geben kann und mein Code darauf nicht reagiert. Deshalb habe ich zusätzlich zu check_winner eine Funktion check_tie geschrieben, die überprüft, ob alle Felder im Spielfeld besetzt sind. Die Umsetzung, damit man Spieler gegen Spieler spielen kann, habe ich nicht fertig geschafft, da ich die Übersicht verloren habe. Ich habe das Projekt dann ohne den Versuch der PvP-Version hochgeladen, damit das Programm funktioniert.

&nbsp;
 
&nbsp;

# Reflexion
n dieser kurzen Lernperiode habe ich mich zum ersten Mal mit Python beschäftigt. Zunächst habe ich mir ein Grundwissen über die Python-Syntax und die Entwicklungsumgebung, in der ich arbeiten muss, erarbeitet. Danach habe ich in VS Code mit meinem Tic-Tac-Toe-Projekt begonnen.Mein größtes Problem war der neue Syntax, vor allem das Fehlen von geschweiften Klammern, was es für mich etwas unübersichtlicher gemacht hat. Dennoch konnte ich mir ein gutes Wissen über Funktionen, Schleifen etc. aneignen und habe einen guten Einblick in Python erhalten. Da das Projekt sehr simpel war und mir viel Spaß gemacht hat, würde ich gerne als Nächstes ein etwas komplexeres Python-Projekt erstellen, das in mehrere Dateien aufgeteilt ist, um die Übersichtlichkeit zu verbessern. Außerdem möchte ich ein Projekt umsetzen, das nicht nur in der Konsole stattfindet – zum Beispiel eine digitale Uhr mit Wecker, Stoppuhr, Timer etc.

&nbsp;
 
&nbsp;



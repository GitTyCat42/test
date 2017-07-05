# test

<h2>Travis CI</h2>
<img src="https://travis-ci.org/jstruzek/test.svg?branch=master" alt=Travis-CI Test-Ergebnis">

<h2>Funktionen</h2>
<h3>1. demofunc()</h4>
demofunc() gibt 42 aus.
<h3>2. demomul(a,b)</h3>
demomul(a,b) gibt das Produkt von a und b aus (a*b).
<h3>3. demopi()</h3>
demopi() berechnet pi mittels Iteration eines 2n-Ecks in 20 Schritten und kommt damit auf 10 richtige Ziffern nach dem Komma.
<h3>4. demofailmul(a,b)</h3>
demofailmul(a,b) ist eine Multiplikation mittels Addition in einer for-Schleife, die falsch initialisiert wurde. Da der Testfall 6 * 7 = 42 bekannt ist, wurden hier Anpassungen vorgenommen, um das Testergebnis zu fälschen.
<h3>5. demomul2(a,b)</h3>
demomul2(a,b) ist ebenfalls eine Multiplikation mittels Addition in einer for-Schleife. (Diesmal richtig.)

<h2>Tests</h2>
Zu jeder Funktion besteht eine Testfunktion mit einem oder mehreren Test-Fällen.
<h3>1. test_demofunc()</h3>
Überprüft nur das Ergebnis.
<h3>2. test_demomul()</h3>
Testet 2*3 und 0*1 auf das richtige Ergebnis und überprüft ob 3*3 >= 9 und kleiner 10 ist.
<h3>3. test_demopi()</h3>
Testet, ob die ersten 10 Stellen von pi richtig berechnet wurden, indem geprüft wird, ob das Ergebnis größer gleich 3,1415926535 und kleiner als 3,1415926526 ist.
<h3>4. test_demofailmul()</h3>
Überprüft ob die Funktion demofailmul bei der Eingabe 6 und 7 als Ergebnis 42 ausgibt. Da nur der eine Fall geprüft wird, merkt der Test nicht, dass die Funktion unabhängig von der errechneten Variable "ergebnis" immer 42 ausgibt.
<h3>5. test_demomul2()</h3>
Testet erst durch zwei verschachtelte Schleifen das vollständige 1 mal 1 und anschließend 10 Produkte von Zufallszahlen bis 1000.

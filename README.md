# Nakonec byla teahle aplikace úplně k ničemu - zadání bylo úplně jiný - ale je mi líto tohle repository mazat, tak tady zůstane :)
 # Hackithon 2024 - SOSTP tým

Ahoj, toto je repository týmu na Hackithon 2024 z Teplické průmyslové školy. Zadání: Převod hlasu na text.

Jsme studenti 2. ročníku střední školy SOSTP a toto je oficiální repository.


# Níže je návod jak začít používat naši aplikaci, zatím je v této formě. Snad již brzy bude jako oficiální webová aplikace.

V závorkách jsou uvedené příkazy, které stačí vložit do terminálu. VŽDY SE UJISTI, ŽE JSI VE SPRÁVNÉM DIRECTORY!

Prvotní nastavení:
1. Nainstaluj si Git
2. Nastav si si jméno a e-mail pro Git
3. Naklonuj toto repository (git clone https://github.com/Apollyus/hackithon-s2t)
4. Volitelný krok (doporučuji) - Udělej si virtual enviroment (python -m venv Nazev)
5. Aktivuj si virtual enviroment (Nazev\Scripts\activate)
6. Nainstaluj requirements.txt (pip install -r requirements.txt)
7. Toť vše, nyní můžeš začít používat a upravovat
8. Když jsi provedl změny, ulož je, commitni je (git commit -m "Zde zadej popis co jsi kde udělal") - Commit a push prováděj prosím, jenom za předpokladu, že jsi si 100% jist, že tvůj kód funguje.
9. A pushni (git push)

*Pokud by jsi si nevěděl s něčím rady, použij AI (ChatGPT, či GitHub Copilot - fungují nejlíp). Pokud si nejsi něčím jistý, zajdi za Vojtou.
**Před každým větším commitem prosím o sdělení zbytku týmu.

# Odkaz pro dokumentaci API Speech to text AI (model whisper-1 myslim) 
https://platform.openai.com/docs/guides/speech-to-text

# Zde je  návod jak zapnout aplikaci: 
1. Nainstaluj Nojde.js z ofiko stránek
2. Nainstaluj nainstaluj dependencies (npm install)
3. V terminále č. 1 přejdi do adresáře backend a spusť main.py (python main.py)
4. V terminále č. 2 spusť React aplikaci (npm run dev)
5. V terminále ti vykočí odkaz na localhost s portem 5173 - http://localhost:5173/
6. Kliknni na na odkaz a máš hotovo :D

* Python (Kódováno na verzi 3.12)

# Hackithon 2024 - SOSTP tým

Ahoj, toto je repository týmu na Hackithon 2024 z Teplické průmyslové školy. Zadání: Převod hlasu na text.

Jsme studenti 2. ročníku střední školy SOSTP a toto je oficiální repository.


# Prvotní setup:
V závorkách jsou uvedené příkazy, které stačí vložit do terminálu. VŽDY SE UJISTI, ŽE JSI VE SPRÁVNÉM DIRECTORY!

1. Stahni Python z MS Store
2. Stáhnout Git
3. Stáhnout Visual Studio Code
4. Stáhnout Python extension pro VS Code
5. Stáhnout Node.js z ofiko stranek a nainstalovat
6. Nastavit mail a jmeno v gitu (git config --global user.name "Your Name"   ;     git config --global user.email "your.email@example.com")
7. Naklonuj si repository projektu, ve VS code otevři nový okno a nový terminál (git clone https://github.com/Apollyus/hackithon-s2t/tree/react-vite) - pozn. Ujisti se, že máš větev react-vite!
8. Premisti se do directory backend (pomoci cd) a vytvor novy env (python -m venv myEnv)
9. Aktivuj si ten env (myEnv\Scripts\activate)
10. Zmen adresu Interpreteru - Otevri pruzkumnika souboru a najdi slozku backend\myEnv\Scripts - tuhle adresu zkopiruj. Ve VS code zmackni CTRL+SHIFT+P zadej python: select interpreter, dej "Enter interpreter path..." a vloz zkopirovanou adresu
11. Vyjed do adresare vys (cd ..) a nainstaluj requirements.txt(pip install -r requirements.txt)
12. Premisti se do directory backend a spust fastapi server(uvicorn main:app --reload) - pockej dokud v terminale nebude:'Startup complete'
13. Otevri novy terminal, stavajici nech bezet! Pomoci cd se premisti do frontend directory(cd ..   ;   cd frontend)
14. Nyni nainstaluj potrebny chujoviny pro react(npm install)
15. Ještě před spuštěním je potřeba doplnit API klíč, ten bohužel nejde sdílet přes GitHub, takže napiš Vojtovi a ten ti ho pošle :D
16. Po úspěšném přidání klíče a správném provedení věcí by ti nyní mělo vše fungovat


*Pokud by jsi si nevěděl s něčím rady, použij AI (ChatGPT, či GitHub Copilot - fungují nejlíp). Pokud si nejsi něčím jistý, zajdi za Vojtou.


# Odkaz pro dokumentaci API Speech to text AI (model whisper-1) 
https://platform.openai.com/docs/guides/speech-to-text

* Před každým větším commitem prosím o sdělení zbytku týmu.

* Python (Kódováno na verzi 3.12)

# Použité technologie:
* FastAPI
* React
* OpenAI API
* Python
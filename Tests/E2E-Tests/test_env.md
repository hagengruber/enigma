Lokale Testumgebung für SeleniumTests erstellen

1. In e2e_test.py unter den else-zweigen seine eigene lokale IP eintragen (localhost funktioniert nicht)
2. Docker-Umgebung vorbereiten:
    2.1. Image builden (im enigma-vz)  
        docker build -t registry.mygit.th-deg.de/sk04333/enigma .
    2.2. Enigma Container starten
        docker-compose up -d
    2.3 Selenium Container starten
        docker run -d -p 4444:4444 -p 7900:7900 --hostname selenium --name selenium --shm-size="2g" selenium/standalone-firefox:latest
3. Test laufen lassen
    3.1. Kommando absetzten
        python.exe -m pytest .\Tests\E2E-Tests\
    3.2. Für jeden weiteren Test Selenium Container neustarten, da dieser nur eine Session zur verfügung stellt und diese nach einem Testlauf geblockt ist
        docker restart selenium
4. Selenium "zuschauen"
    Unter http://localhost:7900/?autoconnect=1&resize=scale&password=secret kann man sehen was alles gekklickt wird usw. sobald man den test gestartet hat
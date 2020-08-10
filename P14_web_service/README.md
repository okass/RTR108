Tika izmēģināts python http serveris globāli un lokāli.
Serveri izveidoja ar `python -m http.server`, kas to izveidoja uz adresses 127.0.0.1:8000
Lai piekļūtu tam no interneta globāli tika izmantots `ngrok` rīks, kas izmanto starpniekserveri, lai padarītu http serveri globālu un nebūtu jārediģē tīkla maršrutētāja iestatījumi.

![Lokālais tīkls](https://raw.githubusercontent.com/okass/RTR108/P14_web_service/local.png)
![Globālais tīkls](https://raw.githubusercontent.com/okass/RTR108/P14_web_service/global.png)
Domotik
=======
Domotik est un projet visant à permettre de contrôller différents appareils électriques à partir de son smartphone. Le premier objectif a été de pouvoir contrôler une lampe éclairant l'avant de ma maison.

Fonctionnement
--------------
Nous utilisons un Raspberry Pi raccordé à un émetteur 433 MHz pour émettre des signaux de commandes vers des prises électriques télécommandés.
Le Raspberry Pi est raccordé au réseau, et fourni une interface Web permettant de commander des interrupteurs.
La "box" est configurée pour relayer les connections sur le port 80 vers le RPi.

Installation
------------
Installer RPi.GPIO
apt-get install python-rpi.gpio
pip install RPi.GPIO

Après avoir cloné le dépot, lancer domotik.py


Configuration
-------------
Section a renseigner

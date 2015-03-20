#!/bin/sh

ARCHIVE_NAME=raspbian_img.zip
echo "#############################################"
echo "Téléchargement de l'image RASPBIAN..."
curl -LsS http://downloads.raspberrypi.org/raspbian_latest > $ARCHIVE_NAME &
echo "Vous allez voire le fichier en cours de téléchargement ainsi que sa taille..."
echo "Lorsque la taille ne varie plus c'est que le téléchargement est terminé."
echo "Lorsque le téléchargement sera terminé appuyez sur Ctrl+C pour continuer."
echo " "
read -p"Appuyez sur une touche pour continuer" a
watch "ls -l $ARCHIVE_NAME"
killall curl
echo "Decompression de l'archive..."
unzip $ARCHIVE_NAME
echo "Décompression terminée."

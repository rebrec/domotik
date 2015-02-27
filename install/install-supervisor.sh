#!/bin/sh

PROJECTNAME=domotik
PROJECTPATH=$( cd $(dirname $0)/.. ; pwd -P )
VENVNAME=venv
VENVREQUIREMENTS=$PROJECTPATH/install/requirements.txt

echo "Prérequis : "
echo "- sudo apt-get install supervisor python-virtualenv"
echo "- installer les outils de dev pour améliorer les performances de tornado"
echo "- sudo apt-get install build-essential python-dev"
echo "###############################"
echo "Ce script va créer le fichier de configuration supervisor qu'il faudra ensuite placer dans /etc/supervisor/conf.d (sur debian)"
echo "Vous allez devois préciser le nom du compte utilisateur qui exécutera le script python."
echo "Ce compte doit posséder les droits d'accès pour emettre des trammes 443Mhz via les pins du Raspberry et doit"
echo "également être à même de lire et d'exécuter les scripts python de ce projet."
echo "###############################"


read -p "Nom du compte utilisateur :" USER

echo ""
echo "Supervisor lancera le $PROJECT_PATH/Controller.py avec l'utilisateur $USER"
echo "Création du fichier de configuration de $PROJECTNAME"

cat << EOF > $PROJECTNAME.conf
[program:$PROJECTNAME]
command=$PROJECTPATH/$VENVNAME/bin/python $PROJECTPATH/Controller.py
user=$USER

EOF
 
echo "##############################"
echo "Le fichier $PROJECTNAME.conf vient d'être généré. Vous devrez le copier dans le dossier de configuration de supervisor."
echo "##############################"
#pushd ./
cd ..
virtualenv $VENVNAME
echo "Le Virtualenv $VENVNAME a été créé"
echo "Entrée dans le virtualenv"
bash -c ". $VENVNAME/bin/activate; pip install -r $VENVREQUIREMENTS;"


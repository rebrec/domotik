#!/bin/sh

PROJECTNAME=domotik
PROJECTPATH=$( cd $(dirname $0)/.. ; pwd -P )
VENVNAME=venv
VENVREQUIREMENTS=$PROJECTPATH/install/requirements.txt

echo "Prérequis : "
echo "- installer supervisor et python-virtualenv"
echo "- installer les outils de dev pour améliorer les performances de tornado"

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

echo << EOF > $PROJECTNAME.conf
[program:$PROJECTNAME]
command=$PROJECT_PATH/$VENVNAME/bin/python $PROJECT_PATH/Controller.py
user=$USER

EOF

echo "##############################"
echo "Le fichier $PROJECTNAME.conf vient d'être généré. Vous devrez le copier dans le dossier de configuration de supervisor."
echo "##############################"
pushd ./
cd ..
virtualenv $VENVNAME
echo "Le Virtualenv $VENVNAME a été créé"
echo "Entrée dans le virtualenv"
source $VENVNAME/bin/activate
echo "Installation des dépendances"
pip install -r $VENVREQUIREMENTS


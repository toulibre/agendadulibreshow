===============================
Agenda du libre midi-pyrénées
===============================

Récupère le RSS de l'`agenda du libre`_ et l'affiche dans une page web.

Utilise la bibliothèque feedparser pour récupérer le flux RSS, et le microframework python Flask_ pour afficher les événements.

Installation
============

Pré-requis
----------

::

    sudo apt-get install python-pip python-virtualenv libapache2-mod-wsgi

Installation
------------

Cloner le repo et créer un virtualenv

::

    git clone https://github.com/toulibre/agendadulibreshow.git
    cd agendadulibreshow
    pip install -r requirements.txt

Lancer l'application

::

    cd agendadulibre
    python app.py

Déploiement avec Apache
-----------------------

Ajouter un virtualhost::

    <VirtualHost *:80>
        ServerAdmin webmaster@mydomain
        ServerName mydomain

        WSGIDaemonProcess /path/to/agendadulibreshow/agendadulibre/agendadulibre.wsgi
        <Directory /opt/agendadulibreshow/agendadulibre>
            WSGIProcessGroup agendadulibre
            WSGIApplicationGroup %{GLOBAL}
            Order allow,deny
            allow from all
        </Directory>

    </VirtualHost>


.. _`agenda du libre`: http://agendadulibre.org/
.. _Flask: http://flask.pocoo.org/

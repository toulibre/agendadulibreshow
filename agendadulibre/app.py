#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  app.py
#  
#  Copyright 2013 numahell <numahell@numajules.net>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.


from flask import Flask, render_template

import parseagenda

app = Flask(__name__)
app.debug = True

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/agenda/")
def agenda():
    agenda_mp_url = "http://www.agendadulibre.org/rss.php?region=16&daylimit=40"
    event_list = parseagenda.Events(agenda_mp_url)
    events = event_list.get_events_from_rss()
    return render_template('agenda.html', events=events)

if __name__ == "__main__":
    app.run()

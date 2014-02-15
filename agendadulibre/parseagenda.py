#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  parseagenda.py
#  
#  Copyright 2013 Emmanuelle Helly <emmanuelle.helly@makina-corpus.com>
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

import feedparser


class Events(object):
    """
    Class for all events from a calendar

    @_data  (private)
    @title  (public)
    @events  (public)
    """
    
    def __init__(self, rss_url=""):
        self.url = rss_url

    def get_events_from_rss(self):
        """
         From an url retrieve events

        @param string rss_url : 
        @return  :
        """
        d = feedparser.parse(self.url)
        return d['entries']


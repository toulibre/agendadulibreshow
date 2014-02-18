#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  parseagenda.py
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

import feedparser


class Events(object):
    """
    Class for all events from a calendar

    @_data  (private)
    @title  (public)
    @events  (public)
    """
    
    def __init__(self, rss_url=""):
        self.rss_url = rss_url

    def get_events_from_rss(self, rss_url=""):
        """
         From an url retrieve events

        @param string rss_url : 
        @return  :
        """
        if rss_url == "" and self.rss_url == "":
            return None
        self.rss_url = rss_url
        d = feedparser.parse(self.rss_url)
        self.title = d['feed']
        
        results = []
        for e in d['entries']:
            event = {}
            event['location'] = e.title.split(' : ')[0]
            event_date_location = e.summary.split('\n\n')[1]
            event['title'] = e.title.split(' : ')[1]
            event['date'] = event_date_location.split('\n')[1]
            event['summary'] = e.summary.split('Description')[1].split('Informations')[0]
            event['content'] = e.content[0].value
            event['link'] = e.links[0]
            results.append(event)

        return results


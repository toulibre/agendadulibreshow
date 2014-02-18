import os
import app
import parseagenda
import unittest
import tempfile

class EventsTestCase(unittest.TestCase):

    def setUp(self):
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()
        self.rss_url = "http://www.agendadulibre.org/rss.php?tag=toulibre"


    # Testing pages
    def test_get_homepage(self):
        homepage = self.app.get('/')
        assert '<h1>Agenda du Libre</h1>' in homepage.data


    # Testing functions
    def test_get_events_from_rss(self):
        events = parseagenda.Events()
        results = events.get_events_from_rss(self.rss_url)
        self.assertTrue(len(results) > 0)
        self.assertTrue(events.title)
        self.assertEqual(results[0]['location'], u'Toulouse')
        self.assertEqual(results[0]['title'], u'Rencontre Logiciels Libres')
        self.assertTrue(results[0]['date'])
        self.assertTrue(results[0]['summary'])
        self.assertTrue(results[0]['content'])

if __name__ == '__main__':
    unittest.main()

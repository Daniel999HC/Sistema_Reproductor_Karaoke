import unittest
from test_transicion_estados import KaraokePlayer

class TestKaraokePlayerTransicionEstados(unittest.TestCase):
    def setUp(self):
        self.player = KaraokePlayer()

    def test_transition_stopped_to_playing(self):
        self.player.add_track("Song 1")
        self.player.play()
        self.assertEqual(self.player.get_state(), 'playing')

    def test_transition_playing_to_paused(self):
        self.player.add_track("Song 1")
        self.player.play()
        self.player.pause()
        self.assertEqual(self.player.get_state(), 'paused')

    def test_transition_paused_to_playing(self):
        self.player.add_track("Song 1")
        self.player.play()
        self.player.pause()
        self.player.play()
        self.assertEqual(self.player.get_state(), 'playing')

    def test_transition_playing_to_stopped(self):
        self.player.add_track("Song 1")
        self.player.play()
        self.player.stop()
        self.assertEqual(self.player.get_state(), 'stopped')

if __name__ == "__main__":
    unittest.main()
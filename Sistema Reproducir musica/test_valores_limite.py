import unittest
from test_valores_limite import KaraokePlayer, PlaylistEmptyError, PlayerStateError

class TestKaraokePlayerValoresLimite(unittest.TestCase):
    def setUp(self):
        self.player = KaraokePlayer()

    def test_add_minimum_length_track(self):
        self.player.add_track("A")
        self.assertIn("A", self.player.playlist)

    def test_add_maximum_length_track(self):
        long_track = "Song " * 100
        self.player.add_track(long_track)
        self.assertIn(long_track, self.player.playlist)

    def test_play_empty_playlist(self):
        with self.assertRaises(PlaylistEmptyError):
            self.player.play()

    def test_next_track_at_last_track(self):
        self.player.add_track("Song 1")
        self.player.play()
        self.player.next_track()
        with self.assertRaises(PlayerStateError):
            self.player.next_track()

if __name__ == "__main__":
    unittest.main()
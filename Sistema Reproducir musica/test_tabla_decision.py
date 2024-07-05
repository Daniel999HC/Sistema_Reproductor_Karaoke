import unittest
from test_tabla_decision import KaraokePlayer, PlaylistEmptyError, PlayerStateError

class TestKaraokePlayerTablaDecision(unittest.TestCase):
    def setUp(self):
        self.player = KaraokePlayer()

    def test_play_with_non_empty_playlist(self):
        self.player.add_track("Song 1")
        self.player.play()
        self.assertEqual(self.player.get_state(), 'playing')

    def test_play_with_empty_playlist(self):
        with self.assertRaises(PlaylistEmptyError):
            self.player.play()

    def test_pause_while_playing(self):
        self.player.add_track("Song 1")
        self.player.play()
        self.player.pause()
        self.assertEqual(self.player.get_state(), 'paused')

    def test_pause_while_not_playing(self):
        with self.assertRaises(PlayerStateError):
            self.player.pause()

    def test_next_track_while_playing_or_paused(self):
        self.player.add_track("Song 1")
        self.player.add_track("Song 2")
        self.player.play()
        self.player.next_track()
        self.assertEqual(self.player.get_current_track(), "Song 2")

    def test_next_track_no_more_tracks(self):
        self.player.add_track("Song 1")
        self.player.play()
        self.player.next_track()
        with self.assertRaises(PlayerStateError):
            self.player.next_track()

if __name__ == "__main__":
    unittest.main()
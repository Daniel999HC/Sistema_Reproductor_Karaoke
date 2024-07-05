# test_equivalencia_particiones.py

import unittest
from test_equivalencia_particiones import KaraokePlayer, InvalidTrackError, PlaylistEmptyError, PlayerStateError
class TestKaraokePlayerEquivalenciaParticiones(unittest.TestCase):
    def setUp(self):
        self.player = KaraokePlayer()

    def test_add_valid_track(self):
        self.player.add_track("Song 1")
        self.assertIn("Song 1", self.player.playlist)

    def test_add_invalid_track(self):
        with self.assertRaises(InvalidTrackError):
            self.player.add_track("")
        with self.assertRaises(InvalidTrackError):
            self.player.add_track(123)

    def test_play_with_tracks(self):
        self.player.add_track("Song 1")
        self.player.play()
        self.assertEqual(self.player.get_state(), 'playing')
        self.assertEqual(self.player.get_current_track(), "Song 1")

    def test_play_without_tracks(self):
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

    def test_stop(self):
        self.player.add_track("Song 1")
        self.player.play()
        self.player.stop()
        self.assertEqual(self.player.get_state(), 'stopped')
        self.assertIsNone(self.player.get_current_track())

    def test_next_track(self):
        self.player.add_track("Song 1")
        self.player.add_track("Song 2")
        self.player.play()
        self.player.next_track()
        self.assertEqual(self.player.get_current_track(), "Song 2")

    def test_next_track_at_end(self):
        self.player.add_track("Song 1")
        self.player.play()
        self.player.next_track()
        with self.assertRaises(PlayerStateError):
            self.player.next_track()

if __name__ == "__main__":
    unittest.main()
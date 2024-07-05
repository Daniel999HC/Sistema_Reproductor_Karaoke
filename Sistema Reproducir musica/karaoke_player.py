# karaoke_player.py

class PlaylistEmptyError(Exception):
    pass

class InvalidTrackError(ValueError):
    pass

class PlayerStateError(Exception):
    pass

class KaraokePlayer:
    def __init__(self):
        self.playlist = []
        self.current_track_index = -1
        self.state = 'stopped'  # possible states: stopped, playing, paused

    def add_track(self, track):
        if isinstance(track, str) and track:
            self.playlist.append(track)
        else:
            raise InvalidTrackError("Track must be a non-empty string")

    def play(self):
        if not self.playlist:
            raise PlaylistEmptyError("Playlist is empty")
        self.current_track_index = 0
        self.state = 'playing'

    def pause(self):
        if self.state == 'playing':
            self.state = 'paused'
        else:
            raise PlayerStateError("Player is not playing")

    def stop(self):
        self.state = 'stopped'
        self.current_track_index = -1

    def next_track(self):
        if self.state in ['playing', 'paused']:
            if self.current_track_index < len(self.playlist) - 1:
                self.current_track_index += 1
                self.state = 'playing'
            else:
                raise PlayerStateError("No more tracks in the playlist")
        else:
            raise PlayerStateError("Player is not playing or paused")

    def get_current_track(self):
        if self.current_track_index == -1:
            return None
        return self.playlist[self.current_track_index]

    def get_state(self):
        return self.state
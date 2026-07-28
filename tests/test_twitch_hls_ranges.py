from __future__ import annotations

import unittest
from unittest.mock import patch

from tools.research import extract_twitch_hls_ranges as hls


class TwitchPlaylistTest(unittest.TestCase):
    def test_fragmented_mp4_map_is_attached_to_segments(self) -> None:
        playlist = b"""#EXTM3U
#EXT-X-MAP:URI=\"init.mp4\"
#EXTINF:2.5,
part-000.m4s
#EXTINF:3.0,
part-001.m4s
"""

        with patch.object(hls, "request_bytes", return_value=playlist):
            segments = hls.parse_media_playlist(
                "https://video.example/path/playlist.m3u8"
            )

        self.assertEqual(2, len(segments))
        self.assertEqual(0.0, segments[0].start)
        self.assertEqual(2.5, segments[1].start)
        self.assertEqual(
            "https://video.example/path/init.mp4", segments[0].init_url
        )
        self.assertEqual(segments[0].init_url, segments[1].init_url)

    def test_map_change_only_affects_following_segments(self) -> None:
        playlist = b"""#EXTM3U
#EXT-X-MAP:URI=init-a.mp4
#EXTINF:1,
a.m4s
#EXT-X-MAP:URI=\"init-b.mp4\"
#EXTINF:1,
b.m4s
"""

        with patch.object(hls, "request_bytes", return_value=playlist):
            segments = hls.parse_media_playlist(
                "https://video.example/root/media.m3u8"
            )

        self.assertEqual(
            [
                "https://video.example/root/init-a.mp4",
                "https://video.example/root/init-b.mp4",
            ],
            [segment.init_url for segment in segments],
        )

    def test_mpeg_ts_playlist_keeps_initialization_empty(self) -> None:
        playlist = b"""#EXTM3U
#EXTINF:4,
000.ts
#EXTINF:4,
001.ts
"""

        with patch.object(hls, "request_bytes", return_value=playlist):
            segments = hls.parse_media_playlist(
                "https://video.example/root/media.m3u8"
            )

        self.assertEqual([None, None], [segment.init_url for segment in segments])


if __name__ == "__main__":
    unittest.main()

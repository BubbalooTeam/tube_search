class VideoSearchFailed(Exception):
    """Raise if a problem occurs while searching for videos in the main functions of the VideoSearch class."""

class VideoNotFound(Exception):
    """Raise if the video to be searched was not found."""
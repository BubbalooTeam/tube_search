from enum import Enum, StrEnum

class TubeEnums(StrEnum):
    HASHTAG_BROWSER = "FEhashtag"
    CHANNEL_ELEMENT = "channelRenderer"
    HASHTAG_ELEMENT = "hashtagTileRenderer"
    PLAYLIST_ELEMENT = "playlistRenderer"
    PLAYLIST_VIDEO_ELEMENT = "playlistVideoRenderer"
    SEARCH_ELEMENT = "AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8"
    SHELF_ELEMENT = "reelShelfRenderer"
    VIDEO_ELEMENT = "videoRenderer"
    CONTINUATION_ITEM = "continuationItemRenderer"
    RICH_ITEM = "richItemRenderer"
    ITEM_SECTION = "itemSectionRenderer"
    PLAYER_RESPONSE = "playerResponse"
    PLAYLIST_PRIMARY_SIDEBAR = "playlistSidebarPrimaryInfoRenderer"
    PLAYLIST_SECONDARY_SIDEBAR = "playlistSidebarSecondaryInfoRenderer"

class TubePathsEnums(Enum):
    HASHTAG_VIDEOS = ["contents", "twoColumnBrowseResultsRenderer", "tabs", 0, "tabRenderer", "content", "richGridRenderer", "contents"]
    HASHTAG_CONTINUATION = ["onResponseReceivedActions", 0, "appendContinuationItemsAction", "continuationItems"]
    CONTENTS = ["contents", "twoColumnSearchResultsRenderer", "primaryContents", "sectionListRenderer", "contents"]
    FALLBACK_CONTENT = ["contents", "twoColumnSearchResultsRenderer", "primaryContents", "richGridRenderer", "contents"]
    CONTINUATION_CONTENT = ["onResponseReceivedCommands", 0, "appendContinuationItemsAction", "continuationItems"]
    CONTINUATION_TOKEN = ["continuationItemRenderer", "continuationEndpoint", "continuationCommand", "token"]
    PLAYLIST_INFO = ["response", "sidebar", "playlistSidebarRenderer", "items"]
    PLAYLIST_VIDEOS = ["response", "contents", "twoColumnBrowseResultsRenderer", "tabs", 0, "tabRenderer", "content", "sectionListRenderer", "contents", 0, "itemSectionRenderer", "contents", 0, "playlistVideoListRenderer", "contents"]

class TubeSearchEnums(StrEnum):
    VIDEO = "EgIQAQ%3D%3D"
    CHANNELS = "EgIQAg%3D%3D"
    PLAYLISTS = "EgIQAw%3D%3D"
    LIVESTREAMS = "EgJAAQ%3D%3D"
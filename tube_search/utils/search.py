from copy import deepcopy
from html import escape
from json import dumps
from typing import Union

from tube_search.core import HTTPCore
from tube_search.exceptions.utils import TubeParseSourceFailed
from tube_search.structs import TubeShelfInfo
from tube_search.utils import TubeEnums, TubePathsEnums, TubeUtils

class YouTubeSearchUtils(HTTPCore, TubeUtils):
    async def _getPayload(self, query: str, language: str, region: str, searchPreferences: str, continuationKey: Union[int, str, dict, None]):
        rBody = deepcopy(self.payload)
        rBody["query"] = query
        rBody["client"] = dict(
            hl=language,
            gl=region,
        )
        if searchPreferences:
            rBody["params"] = searchPreferences
        if continuationKey:
            rBody["continuation"] = continuationKey
        rBodyEncoded = dumps(rBody).encode('utf-8')
        return rBodyEncoded

    async def search(
        self,
        query: str,
        language: str,
        region: str,
        searchPreferences: str,
    ):
        rBody = await self._getPayload(query, language, region, searchPreferences, None)
        r = await self.http.post(
            url="https://www.youtube.com/youtubei/v1/search?key={key}".format(key=TubeEnums.SEARCH_ELEMENT),
            data=rBody,
            headers={
                "Content-Type": "application/json; charset=utf-8",
                "Content-Length": str(len(rBody)),
                "User-Agent": self.userAgent
            },
        )
        return r.json()

    def parseSourceResponse(self, response: dict, continuationKey: Union[int, str, dict, None]):
        try:
            if not continuationKey:
                rContent = self.getValue(response, TubePathsEnums.CONTENTS.value)
            else:
                rContent = self.getValue(response, TubePathsEnums.CONTINUATION_CONTENT.value)

            if rContent:
                for e in rContent:
                    if TubeEnums.ITEM_SECTION.value in e.keys():
                        rS = self.getValue(e, [TubeEnums.ITEM_SECTION.value, "contents"])
                    if TubeEnums.CONTINUATION_ITEM.value in e.keys():
                        continuationKey = self.getValue(e, TubePathsEnums.CONTINUATION_TOKEN.value)
            else:
                rS = self.getValue(response, TubePathsEnums.FALLBACK_CONTENT)
                continuationKey = self.getValue(rS[-1], TubePathsEnums.CONTINUATION_TOKEN.value)
            return rS, continuationKey
        except:
            raise TubeParseSourceFailed("Failed to format the YouTube source data!")
    
    def getShelfComponent(self, element: dict) -> TubeShelfInfo:
        shelf = element[TubeEnums.SHELF_ELEMENT.value]
        return TubeShelfInfo(
            title=self.getValue(shelf, ["title", "simpleText"]),
        )
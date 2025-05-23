from copy import deepcopy
from json import dumps
from typing import List, Optional, Union

from tube_search.core import HTTPCore
from tube_search.exceptions.utils import TubeParseSourceFailed
from tube_search.structs import TubeShelfInfo
from tube_search.utils import TubeEnums, TubePathsEnums, TubeUtils

class YouTubeSearchUtils(HTTPCore, TubeUtils):
    async def _getPayload(self, query: str, language: str, region: str, searchPreferences: Optional[str], continuationKey: Optional[Union[int, str, dict, None]]) -> bytes:
        """
        This asynchronous method constructs the payload for a search request.

        Args:
            query - (str): The search term provided by the user. This is the main subject of the search (e.g., 'Elektronomia - NCS').
            language - (str): The language code indicating the desired language for the search results (e.g., 'en-US' for English (USA), 'pt-BR' for Portuguese (Brazil).)
            region - (str): The region code specifying the geographic area for the search results (e.g., 'US' for United States, 'BR' for Brazil).
            searchPreferences - Optional(str): Additional search parameters or preferences, often encoded as a string. This allows for more specific search configurations.
            continuationKey - Optional(Union[int, str, dict, None]): A key used for pagination or to retrieve the next set of search results. It can be an integer, a string, a dictionary, or None if it's the initial request.

        Returns:
            bytes: A UTF-8 encoded JSON string representing the request payload. This payload is typically sent to a search.
        """

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
        searchPreferences: Optional[str],
    ) -> dict:
        """
        This asynchronous method make a request in 'youtube.com', using the parameters returned in bytes from the `self._getPayload(...)` function.

        Args:
            query - (str): The search term provided by the user. This is the main subject of the search (e.g., 'Elektronomia - NCS').
            language - (str): The language code indicating the desired language for the search results (e.g., 'en-US' for English (USA), 'pt-BR' for Portuguese (Brazil).)
            region - (str): The region code specifying the geographic area for the search results (e.g., 'US' for United States, 'BR' for Brazil).
            searchPreferences - Optional(str): Additional search parameters or preferences, often encoded as a string. This allows for more specific search configurations.
        
        Returns:
            dict: Result of the YouTube request, compressed into a dictionary for ease.
        """

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

    def parseSourceResponse(self, response: dict, continuationKey: Optional[Union[int, str, dict, None]]) -> List[dict]:
        """
        Extracts the relevant content and next [continuationKey] from a raw response.

        Args:
            response - (dict): The original raw response from scrapper.
            continuationKey - Optional(Union(int, str, dict, None)): A key used for pagination or to retrieve the next set of search results. It can be an integer, a string, a dictionary, or None if it's the initial request.

        Returns:
            List[dict]: The list of parsed responses for use.
        """

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
        """
        Extracts information about a shelf component from a dictionary.

        Args:
            element - (dict): A dictionary containing data for various components, expected to have a shelf element.
        
        Returns:
            TubeShelfInfo: Shelf information compressed into dataclass to be better attributed.
        """

        shelf = element[TubeEnums.SHELF_ELEMENT.value]
        return TubeShelfInfo(
            title=self.getValue(shelf, ["title", "simpleText"]),
        )
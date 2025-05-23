from httpx import AsyncClient, Timeout

class HTTPCore:
    def __init__(self):
        self.http = AsyncClient(
            http2=True,
            timeout=Timeout(
                timeout=20,
                pool=None,
            ),
        )
        self.payload = dict(
            context=dict(
                client=dict(
                    clientName="WEB",
                    clientVersion="2.20250522.20.39",
                    newVisitorCookie=True,
                ),
                user=dict(
                    lockedSafetyMode=False,
                )
            )
        )
        self.userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:137.0) Gecko/20100101 Firefox/137.0"
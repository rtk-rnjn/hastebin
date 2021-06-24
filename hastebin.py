from aiohttp import ClientSession
from datetime import datetime
from requests import request


async def AsyncPaste(text: str, language: str = None):
    """
		Return an online bin of given text. Kinda simple [Async]
		"""

    async with ClientSession() as aioclient:
        post = await aioclient.post("https://hastebin.com/documents",
                                    data=text)
        if post.status == 200:
            response = await post.text()
            return {
                "success": True,
                "status": post.status,
                "url": f"https://hastebin.com/{response[8:-2]}",
                "created_at": datetime.utcnow(),
                "code": response[8:-2],
            }

        # Rollback bin
        post = await aioclient.post(
            "https://bin.readthedocs.fr/new",
            data={
                "code": text,
                "lang": f'{language if language else "txt"}'
            },
        )
        if post.status == 200:
            return {
                "success": True,
                "status": post.status,
                "url": post.url,
                "created_at": datetime.utcnow(),
                "code": str(post.url).split("/")[-1],
            }


def Paste(text: str, language: str = None):
    """
		Return an online bin of given text. Kinda simple [Normal]
		"""
    post = request("POST", "https://hastebin.com/documents", data=text)
    if post.status_code == 200:
        response = post.text
        return {
            "success": True,
            "status": post.status_code,
            "url": f"https://hastebin.com/{response[8:-2]}",
            "created_at": datetime.utcnow(),
            "code": response[8:-2],
        }

    # Rollback bin
    post = request(
        "POST",
        "https://bin.readthedocs.fr/new",
        data={
            "code": text,
            "lang": f'{language if language else "txt"}'
        },
    )
    if post.status_code == 200:
        return {
            "success": True,
            "status": post.status_code,
            "url": post.url,
            "created_at": datetime.utcnow(),
            "code": str(post.url).split("/")[-1],
        }

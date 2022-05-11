from aiohttp import ClientSession
from requests import request


async def AsyncPaste(text: str, language: str = None) -> str:
    """
    Async method to store online text for a short period of time

    Args:
        text (str): The text to paste.
        language (str, optional): Syntax. Defaults to 'txt' if None is passed in.

    Returns:
        str: Returns the link
    """

    async with ClientSession() as aioclient:
        post = await aioclient.post("https://hastebin.com/documents",
                                    data=text)
        if post.status == 200:
            response = await post.text()
            return f"https://hastebin.com/{response[8:-2]}"
        
        # Rollback bin
        post = await aioclient.post(
            "https://bin.readthedocs.fr/new",
            data={
                "code": text,
                "lang": language or "txt",
            },
        )
        if post.status == 200:
            return post.url

def Paste(text: str, language: str = None) -> str:
    """
    Synchronize method to store online text for a short period of time.
    
    Args: 
        text (str): The text to paste.
        language (str, optional): Syntax. Defaults to 'txt' if None is passed in.
    
    Returns:
        str: Returns the link
    """
    post = request("POST", "https://hastebin.com/documents", data=text)
    if post.status_code == 200:
        response = post.text
        return f"https://hastebin.com/{response[8:-2]}"

    # Rollback bin
    post = request(
        "POST",
        "https://bin.readthedocs.fr/new",
        data={
            "code": text,
            "lang": language or "txt",
        },
    )
    if post.status_code == 200:
        return post.url

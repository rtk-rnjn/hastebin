# hastebin.py
A simple Hastebin Python wrapper. This is kinda useless but its important.

Its super easy to use, supports both `aiohttp 3.7.4.post0` and `requests 2.25.1` module.
```python
from hastebin import Paste

def main():
    text = input("Enter your text: ")
    # This is sample text
    data = Paste(text, 'txt')
    print(data)

if __name__ == '__main__':
    main()
```
```python
import asyncio
from hastebin import AsyncPaste

async def main():
    text = input("Enter your text: ")
    # This is sample text
    data = await AsyncPaste(text, 'txt')
    print(data)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
```
Found Error? Have Suggestion? Consider opening up an issue!

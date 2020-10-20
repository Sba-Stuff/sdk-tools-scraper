# sdk-tools-scraper

As An Android Application Developer, It is very difficult for me to develop applications with different build tools. Moreover, I live in country where internet facility is not good. One of the ways to tackle such situations is that one can download all build tools before hand. I did the same. Instead of going individualy on every link to download file, I made a scrapper that visit site and check for windows build tools to download build tools for windows SDK. It creates folders and save the SDK build tools files in there. Easy isn't it?

How To Run?

Make a Folder Named "SDKTools" With SDKBtoolsScraper.py.
Make sure python.exe, SDKTools folder and SDKBtoolsScraper.py will be in the same place.
Open CMD at same place. And then type: python.exe SDKBtoolsScraper.py
Leave the rest on script.

Kind Note:
If you want to download build tools for linux, just replace "windows" with "linux" in scrapelinks function

If you want to download build tools for Mac, just replace "windows" with "macosx" in scrapelinks function

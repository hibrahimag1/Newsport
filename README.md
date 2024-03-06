# Newsport
Newsport is a small demo of a news-gathering application, that gives its user the latest news on selected subjects from local news reporters.

Newsport is a Python application that uses web-scraping. Since it is designed as a demo version, and not a full-scale application, it only scrapes news from one website: [zenicablog.com](https://www.zenicablog.com/). Taking into account their copyright policy I do not have permission to use this application for commercial use and this app's purpose is solely educational and demonstrative. If someone decides to use this application for such purposes, please contact the website personnel for permission. 

```News.py``` is the file where the web-scraping mechanism is implemented. Thanks to the websites manually structured html it wasn't complicated to scrape it. It features the ```welcome()``` function, which runs Newsport in the terminal, as that was how the application was originally meant to be displayed. The GUI was developed a long time after.

```menu.py``` is the GUI part of the application built in PySimpleGui. I choose PSG for it's simplicity and how easy it was to build a GUI from scratch with no prior knowledge of the library. For the most part it was sufficient for my needs, except for one thing. It takes a lot of time to load the application (5+ seconds) due to the fact that all the web-articles are being scraped at once when starting the application. I would have fixed that by scraping only the articles on the subject the user has chosen, but due to the way the layout of the window works in PSG that wasn't possible.

When I started to make the GUI I used fixed window and element dimensions and haven't changed it yet, maybe I will in the future, but for now it will probably look bad on most machines. Overall the app functionality and design took less than a week's worth of time, and is no where near completion. A few ideas/fixes I have in mind are:
- element dimensions based on screen % and not fixed
- add more news sources and subjects
- be able to view older news, upto a week old
- potentially add images next to news titles/links
- add an AI that summarises articles without the need to enter them
- add loading screen when waiting for something to execute

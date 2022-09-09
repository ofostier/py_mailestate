from ast import arg
import asyncio
from pyppeteer import launch
from pyppeteer_stealth import stealth
import time, os
from common import tmp_folder

if os.path.isdir(tmp_folder) == False:
    os.mkdir(tmp_folder)

async def main():
    # launch chromium browser in the background
    browser = await launch(
        args = [
        '--no-sandbox',
        '--disable-setuid-sandbox',
        '--disable-infobars',
        '--window-position=0,0',
        '--ignore-certifcate-errors',
        '--ignore-certifcate-errors-spki-list',
        '--user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3312.0 Safari/537.36"'
        ],
        headless=False,
        ignoreHTTPSErrors=True,
        userDataDir='./tmp'
    )
    # open a new tab in the browser
    #page = await browser.newPage()
    page = (await browser.pages())[0]
    await stealth(page)

    # add URL to a new page and then open it
    # await page.goto("https://www.seloger.com/")
    await page.goto("https://bot.sannysoft.com/")
    # create a screenshot of the page and save it
    await page.screenshot({"path": "python.png"})
    # close the browser
    # await browser.close()
    time.sleep(15)
print("Starting...")
asyncio.get_event_loop().run_until_complete(main())
print("Screenshot has been taken")
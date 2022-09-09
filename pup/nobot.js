// puppeteer-extra is a wrapper around puppeteer,
// it augments the installed puppeteer with plugin functionality
const puppeteer = require('puppeteer-extra');

// add stealth plugin and use defaults (all evasion techniques)
const StealthPlugin = require('puppeteer-extra-plugin-stealth');
puppeteer.use(StealthPlugin());

const url = process.argv[2];
if (!url) {
    throw "Please provide a URL as the first argument";
}

// puppeteer usage as normal
puppeteer.launch({ headless: true }).then(async browser => {
  console.log('Check the bot tests..');
  //const page = await browser.newPage();
  const page = (await browser.pages())[0];
  //await page.goto('https://bot.sannysoft.com');
  await page.goto(url);
  await page.waitForTimeout(5000);
  await page.screenshot({ path: 'bot-test-result.png', fullPage: true });
  await browser.close();
  console.log(`All done, check the bot result screenshot. `);
});
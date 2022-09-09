const puppeteer = require('puppeteer');
const fs = require('fs');

const url = process.argv[2];
if (!url) {
    throw "Please provide a URL as the first argument";
}

async function run () {
    const browser = await puppeteer.launch();
    //const page = await browser.newPage();
    const page = (await browser.pages())[0];

    // Simulate 2 cookies assertion: a=1, b=2
    await page.goto('http://httpbin.org/cookies/set?a=1&b=2');

    const cookies = await page.cookies();
    const cookieJson = JSON.stringify(cookies);

    // And save this data to a JSON file
    fs.writeFileSync('httpbin-cookies.json', cookieJson);
    
    await page.goto(url);
    await page.screenshot({path: 'screenshot.png'});
    browser.close();
}
run();

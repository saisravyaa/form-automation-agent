from playwright.async_api import async_playwright

async def fill_sample_form(address_info):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        await page.goto("https://www.selenium.dev/selenium/web/web-form.html")
        await page.fill('input[name="my-text"]', address_info.get("city", "DefaultCity"))
        await page.fill('input[name="my-password"]', address_info.get("zip", "00000"))

        await page.screenshot(path="filled_form.png")
        print("✅ Screenshot saved")

        await page.wait_for_timeout(900000)
        await browser.close()
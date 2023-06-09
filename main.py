from playwright.sync_api import sync_playwright
from time import sleep
url_l = "https://www.instagram.com/accounts/login/"
url_p = "https://www.instagram.com/p/CsyvH4pA4kF/"

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(url_l)
    print(page.title())

    page.locator('//*[@id="loginForm"]/div/div[1]/div/label/input').fill("userS")
    page.locator('//*[@id="loginForm"]/div/div[2]/div/label/input').fill("pass")
    page.locator('//*[@id="loginForm"]/div/div[3]/button').click()

    sleep(10)
    print(page.title())
    sleep(5)

    page.goto(url_p)
    sleep(15)
    print(page.title())


    while True:
        try:
            page.locator('//*[@id="mount_0_0_ad"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[2]/div/div/ul/li/div/button').click()
            print(page.locator('//*[@id="mount_0_0_ad"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[2]/div/div').inner_html())
        except:
            e = page.locator('//*[@id="mount_0_0_ad"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[2]/div/div')
            file = open("result.txt", "a")
            a = e.inner_html()
            file.write(str(a))
            file.close()
            break
        sleep(3)
    browser.close()
from selenium import webdriver
from urllib.request import urlopen
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import os

if not os.path.isdir("도라에몽/"):
    os.makedirs("도라에몽/")

driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")

search = "도라에몽"
elem = driver.find_element_by_name("q")
elem.send_keys(search)
elem.send_keys(Keys.RETURN)

SCROLL_PAUSE_TIME = 1

last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")

    if new_height == last_height:
        try:
            driver.find_element_by_css_selector(".mye4qd").click()
        except:
            break
    last_height = new_height

images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
count = 1
for image in images:
    try:
        image.click()
        time.sleep(2)
        imgUrl = driver.find_element_by_xpath("//*[@id='Sva75c']/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img").get_attribute('src')
        urllib.request.urlretrieve(imgUrl, "도라에몽/" + search + "_" + str(count) + ".jpg")
        print("Image saved: 도라에몽_{}.jpg".format(count))
        count += 1
    except:
        pass

driver.close()
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

# # 브라우저 꺼짐 방지 옵션
# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(options=chrome_options)

# # 웹페이지 해당 주소 이동
# driver.get("https://www.naver.com")

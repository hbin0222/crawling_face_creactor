import os
import tkinter as tk
from tkinter import filedialog
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
#브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

#웹페이지 해당 주소 이동
driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")

def crawling():
    search_query = search_entry.get() #검색어
    dir_query = dir_entry.get() #디렉토리 경로

    #크롤링한 파일 모아둘 디렉토리 생성
    if not os.path.isdir(f"{dir_query}/{search_query}/"): #디렉토리에 폴더가 없을경우 생성
        os.makedirs(f"{dir_query}/{search_query}/")
        print(f"{search_query}디렉토리 생성!")
    else:
        print(f"{search_query}디렉토리가 존재합니다.!")
    #구글 검색창 선택
    element = driver.find_element(By.NAME, "q") #find_element_by_name메서드가 삭제되고 대체되는 방법
    element.send_keys(search_query)#입력받은 검색어 입력
    element.send_keys(Keys.RETURN)# 검색시작

    #모든 이미지를 불러올 시간을 주어야함
    time.sleep(2)

    imgs = driver.find_elements(By.CSS_SELECTOR, ".rg_i")#이미지들을 모두 선택
    # with open('imgs.html', "w", encoding='utf8') as f:
    #     for img in imgs:
    #       f.write(str(img.get_attribute("outerHTML")) + "\n")
    cnt=0
    for img in imgs:
        try:
            img.click()
            time.sleep(0.5)
            img_element = driver.find_element(By.CSS_SELECTOR, "img.r48jcc.pT0Scc.iPVvYb")
            imgUrl = img_element.get_attribute("src")
            print(imgUrl)
            urllib.request.urlretrieve(imgUrl, f"{dir_query}/{search_query}/{search_query}_" + str(cnt) + ".jpg")
            cnt += 1
            if cnt >= 5:
                break
        except:
            print("img error")


#GUI 생성
window = tk.Tk()
window.title("Images Crawling")
window.geometry("300x300+500+500")#창 크기 및 출현위치설정

#디렉토리 생성
dir_label = tk.Label(window, text="디렉토리")
dir_label.pack()
dir_var = tk.StringVar() #문자열 객체 생성
dir_entry = tk.Entry(window, textvariable=dir_var)
dir_entry.pack()

def choose_dir():
    sel_dir = filedialog.askdirectory()
    dir_var.set(sel_dir)

dir_btn = tk.Button(window, text="선택", command=choose_dir)
dir_btn.pack()

#검색어 입력
search_label = tk.Label(window, text="검색어")
search_label.pack()
search_entry = tk.Entry(window)
search_entry.pack()

def perform():
    crawling()
search_btn = tk.Button(window, text="검색", command=perform)
search_btn.pack()

window.mainloop()
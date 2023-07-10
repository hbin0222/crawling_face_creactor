import os
import tkinter as tk
from tkinter import filedialog
import requests
from bs4 import BeautifulSoup
# import cv2

def search_and_save_images():
    search_query = search_entry.get()
    directory_path = directory_var.get()
    if directory_path:
        crawl_and_save_images(search_query, directory_path)

def crawl_and_save_images(search_query, directory_path):
    url = f"https://www.google.com/search?q={search_query}&tbm=isch"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    image_elements = soup.find_all("img")

    os.makedirs(directory_path, exist_ok=True)

    count = 0
    for img_element in image_elements:
        if count >= 10:
            break
        image_url = img_element["src"]
        try:
            response = requests.get(image_url, headers=headers)
            response.raise_for_status()

            image_path = os.path.join(directory_path, f"{search_query}_{count}.jpg")
            with open(image_path, "wb") as f:
                f.write(response.content)

            count += 1

        except requests.exceptions.RequestException as e:
            print(f"Error downloading image: {e}")

# GUI 생성
window = tk.Tk()
window.title("Image Crawler")
window.geometry("300x250")

# 디렉토리 선택
directory_label = tk.Label(window, text="디렉토리:")
directory_label.pack()
directory_var = tk.StringVar()
directory_entry = tk.Entry(window, textvariable=directory_var)
directory_entry.pack()

def choose_directory():
    selected_directory = filedialog.askdirectory()
    directory_var.set(selected_directory)

directory_button = tk.Button(window, text="디렉토리 선택", command=choose_directory)
directory_button.pack()

# 검색어 입력
search_label = tk.Label(window, text="검색어:")
search_label.pack()
search_entry = tk.Entry(window)
search_entry.pack()

def perform_search():
    search_and_save_images()

search_button = tk.Button(window, text="검색", command=perform_search)
search_button.pack()

window.mainloop()

import tkinter as tk
from tkinter import filedialog

def choose_directory():
    directory_path = filedialog.askdirectory(title="Select Directory")
    if directory_path:
        directory_label.config(text=f"디렉토리: {directory_path}")

# GUI 생성
window = tk.Tk()
window.title("Image Crawler")
window.geometry("500x500")
window.configure(bg="white")  # 배경색을 흰색으로 설정

# 디렉토리 선택 버튼
directory_button = tk.Button(window, text="디렉토리 선택", command=choose_directory)
directory_button.pack()

# 디렉토리 표시 레이블
directory_label = tk.Label(window, text="디렉토리: ", background="white")  # 배경색을 흰색으로 설정
directory_label.pack()

# 검색어 입력 레이블
search_label = tk.Label(window,text="검색어:", bg="white")  # 배경색을 흰색으로 설정
search_label.pack()

# 검색어 입력 필드
search_entry = tk.Entry(window, width=100, bg="white")  # 배경색을 흰색으로 설정
search_entry.pack()

# 검색 버튼
search_button = tk.Button(window, text="검색", bg="black")  # 배경색을 흰색으로 설정
search_button.pack()

window.mainloop()

import json
import tkinter as tk
from tkinter import messagebox

# 파일 경로 설정
GONG_PATH = "json/gong.json"
SANTA_PATH = "json/santa.json"
TO_BE_SANTA_PATH = "json/tobesanta.json"


##### [게임 시작] 버튼을 눌렀을 때 실행될 함수 #####
def start_game():
    try:
        # 1. [Read] gong.json 읽어오기
        with open(GONG_PATH, 'r', encoding='utf-8') as f:
            gong_data = json.load(f)
        
        # 2. [Create] tobesanta.json 생성하고 gong_data 데이터 불러오기
        with open(TO_BE_SANTA_PATH, 'w', encoding='utf-8') as f:
            json.dump(gong_data, f, ensure_ascii=False, indent=4)
            
        # 3. 화면 전환을 위해 현재 화면의 모든 요소(위젯)를 지우기
        for widget in root.winfo_children():
            widget.destroy()
            
        # 4. 다음 화면 UI 그리기 (2번 시나리오)
        show_main_playground()
        
    except FileNotFoundError:
        messagebox.showerror("에러", "json 폴더나 원본 파일이 없습니다!")


##### [2번 화면] 게임 시작 후 출력되는 화면 #####
def show_main_playground():
    #[산타 조건 확인] / [공욱재 상태 확인] 버튼이 있는 메인 게임 화면
    label = tk.Label(root, text="공욱재의 상태와 산타의 조건을 확인해보세요.", font=("함초롬바탕", 15))
    label.pack(pady=(100, 50))
    
    # 여기에 [산타 조건 확인] 버튼 등을 추가하면 되겠죠?
    btn_santa = tk.Button(root, text="산타 조건 확인", width=20)
    btn_santa.pack(pady=5)
    
    btn_gong = tk.Button(root, text="공욱재 상태 확인", width=20)
    btn_gong.pack(pady=5)




##### UI 초기 설정  #####
root = tk.Tk()
root.title("공욱재 산타 만들기")
root.geometry("600x600") # 창 크기 설정

##### 시작 화면 구성 #####
# 제목
title = tk.Label(root, text="공욱재 삥뜯기 게임", font=("함초롬바탕", 20, "bold"))
title.pack(pady=(100, 50)) # pack은 화면에 배치하는 함수입니다. pady는 상하 여백입니다.

# 설명글
description = """
305호실의 악마 공욱재는 지극히 평범한 한국인입니다.
공욱재를 산타클로스로 만들어서 선물을 뜯어내 봅시다.

산타클로스는 특징이 있습니다.
공욱재의 현재 상태를 
산타클로스의 특징에 부합하도록 수정해보세요.
모든 요건을 산타클로스의 조건과 통일시키면
공욱재가 공산타로 변신합니다.
"""
desc_label = tk.Label(root, text=description, font=("함초롬바탕", 12, "bold"), justify="center") # justify는 정렬입니다.
desc_label.pack(pady=(0, 50))

# [게임 시작] 버튼
# command=start_game 은 버튼을 누르면 위에서 만든 함수를 실행하라는 뜻입니다.
start_btn = tk.Button(root, text="[ 게임 시작 ]", font=("함초롬바탕", 12, "bold"), command=start_game, width=20, height=2, bg="red", activebackground="darkred", fg="white", activeforeground="white", cursor="hand2")
start_btn.pack(pady=20)




# 프로그램 실행 (이게 있어야 창이 안 닫히고 유지됩니다)
if __name__ == "__main__":
    # root.destroy()
    root.mainloop()
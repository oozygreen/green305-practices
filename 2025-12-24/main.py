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







def read_santa_condition():
    # 1. 기존에 그려진 표가 있다면 청소 (지우기)
    for widget in santa_display_area.winfo_children():
        widget.destroy()

    # 2. 데이터 불러오기 (Read)
    try:
        with open(SANTA_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # 3. 보여주고 싶은 데이터 정리 (평탄화 작업)
        # 딕셔너리가 중첩되어 있으니 보여줄 것들만 리스트로 뽑아봅시다.
        status = data["status"]
        look = status["look"]
        clothes = status["clothes"]
        items = data["items"]
        
        table_data = [
            # 헤더
            ("항목", "내용"),
            # 내용
            ("국적", status["nationality"]),
            ("머리색", look["hair_color"]),
            ("수염색", look["beard"]["beard_color"]),
            ("수염길이", look["beard"]["beard_length"]),
            ("체형", look["body"]),
            ("옷_모자", clothes["hat"]),
            ("옷_아우터", clothes["outer"]),
            ("옷_상의", clothes["top"]),
            ("옷_하의", clothes["bottom"]),
            ("옷_신발", clothes["shoes"]),
            ("옷_장갑", clothes["gloves"]),
            ("휴대물품", items["bag"]),
            ("애완동물", items["pets"]),
            ("자가용", items["car"])
        ]

        # 4. 표 그리기 (grid 활용)
        # 
        for i, (key, value) in enumerate(table_data):
            # 항목 칸 (열 0)
            cell_key = tk.Label(santa_display_area, text=key, font=("함초롬바탕", 10, "bold"), borderwidth=1, relief="solid", width=10, height=1)
            cell_key.grid(row=i, column=0, sticky="nsew")
            
            # 내용 칸 (열 1)
            cell_val = tk.Label(santa_display_area, text=value, font=("함초롬바탕", 10), borderwidth=1, relief="solid", width=15, height=1)
            cell_val.grid(row=i, column=1, sticky="nsew")

    except Exception as e:
        messagebox.showerror("에러", f"데이터를 읽는 중 오류 발생: {e}")


##### [2번 화면] 게임 시작 후 출력되는 화면 #####
def show_main_playground():
    #[산타 조건 확인] / [공욱재 상태 확인] 버튼이 있는 메인 게임 화면
    label = tk.Label(root, text="공욱재의 상태와 산타의 조건을 확인해보세요.", font=("함초롬바탕", 15, "bold"))
    label.pack(pady=(50, 20))
    
    # 1. 전체를 감싸는 큰 메인 프레임 (좌/우를 담을 그릇)
    main_container = tk.Frame(root)
    main_container.pack(expand=True, fill="both", padx=20)

    # 2. 왼쪽 구역 (산타용)
    left_section = tk.Frame(main_container)
    left_section.pack(side="left", expand=True, fill="both", anchor="n")

    # 4. [산타 조건 확인] 버튼 (프레임 안에 배치)
    # root가 아니라 button_frame에 속하게 만듭니다.
    btn_santa = tk.Button(left_section, text="산타 조건 확인", command=read_santa_condition, font=("함초롬바탕", 12, "bold"), bg="red", activebackground="darkred", fg="white", activeforeground="white", width=15, cursor="hand2")
    btn_santa.pack(side="top", padx=50, pady=(0, 20), anchor="n")
    
    # 산타 표가 그려질 곳
    global santa_display_area 
    santa_display_area = tk.Frame(left_section)
    santa_display_area.pack(expand=True, fill="both", padx=50)

    # 3. 오른쪽 구역 (공욱재용)
    right_section = tk.Frame(main_container)
    right_section.pack(side="left", expand=True, fill="both", anchor="n")
    
    # 5. [공욱재 상태 확인] 버튼 (프레임 안에 배치)
    btn_gong = tk.Button(right_section, text="공욱재 상태 확인", font=("함초롬바탕", 12, "bold"), bg="green", activebackground="darkgreen", fg="white", activeforeground="white", width=15, cursor="hand2")
    btn_gong.pack(side="top", padx=50, pady=(0, 20), anchor="n")

    # 공욱재 표가 그려질 곳
    global gong_display_area
    gong_display_area = tk.Frame(right_section)
    gong_display_area.pack(expand=True, fill="both", padx=50)




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
    root.mainloop()
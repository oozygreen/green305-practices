import tkinter as tk

# tkinter 창 생성
root = tk.Tk()

# 창 제목 설정
root.title("HelloWorld!")

# 창 크기 설정
root.geometry("300x200")

# "HelloWorld!" 텍스트를 표시하는 Label 생성
label = tk.Label(root, text="HelloWorld!", font=("Arial", 20))
label = tk.Label(root, text="Hello 재형!", font=("sanserif", 12))
label.pack(pady=50)  # 위젯 배치 및 여백 설정

# tkinter 이벤트 루프 실행
root.mainloop()
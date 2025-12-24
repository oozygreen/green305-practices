a = ["김수빈", "고경명", "박의천", "유효현", "김민우", "이세한", "김재형"]
b = ["김동찬", "정승훈", "박지수", "송우인", "신재혁", "손예진", "김노현", "전민권"]

a.append("공욱재")

bool = len(a) == len(b)

if bool == True :
    print(bool)
    a.append("김언수")
    b.append("김언수")
    print(a)
    print(b)
else :
    print(bool)
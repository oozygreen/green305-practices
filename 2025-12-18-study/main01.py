pc_cafe = {
    "food" : ["라면", "과자", "볶음밥", "햄버거", "샌드위치"]
}

# <<< 카페에 있는 음식 목록 조회 >>>
for food_name in pc_cafe["food"]:
    print(food_name)

for food_index in range(len(pc_cafe["food"])):
    # print(food_index)
    # print(pc_cafe['food'][food_index])
    print(food_index, pc_cafe['food'][food_index])

user_choice = input("먹고 싶은 음식은? ")

# 만약에 인풋에 입력된 값이 피씨카페의 푸드 배열에 없는 항목이라면
#     죄송하지만 준비중입니다. 나중에 추가할게요.
# 배열에 있는 항목이라면
#     5분내로 준비해서 드리겠습니다.

# ------------------------------------------------
# 1. 나의 코드
# ------------------------------------------------
# if user_choice not in pc_cafe['food'] :
#     print("'" + user_choice + "' 은/는 현재 메뉴에 존재하지 않습니다. 추후에 메뉴를 추가하겠습니다.")
# else :
#     print("'" + user_choice + "'을/를 주문하셨습니다. 5분 내로 준비해서 안내해 드리겠습니다.")


# ------------------------------------------------
# 2. 강사님 코드
# ------------------------------------------------
for food_item in range(len(pc_cafe["food"])):
    if pc_cafe["food"][food_item] == user_choice:
        print(pc_cafe["food"][food_item] + " 음식을 준비하겠습니다.")
    else:
        print("아쉽게도 그 음식은 없습니다.")

        user_yes_no = input("하지만, 내일 준비할까요? (네 / 아니오)")

        if user_yes_no == "네" :
            pc_cafe["food"].append(user_choice)
        else :
            print(pc_cafe["food"])
            print("종료") 

# food_item은 for 문에서 선언한 변수로 in 뒤의 구절에 따라 값이 정해짐
# for food_item in pc_cafe["food"]:
#     print(food_item)

# * 1. 카페 음식 정의하기
# * 2. 카페 음식 목록 조회하기
# * 3. 사용자가 먹고 싶은 음식 선택하기
# * 4. 사용자가 선택한 음식이 카페에 있는지 확인하기
# * 5. 음식이 있으면 준비하겠다고 알리기
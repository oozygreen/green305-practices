import json
import random
import os

# 데이터 파일 경로
DB_FILE = "data.json"

def load_data():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_data(data):
    with open(DB_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def get_next_id(data):
    if not data:
        return 1
    return max(item['id'] for item in data) + 1

# 1-1. Create: 꽃씨 심기
def create_seed():
    data = load_data()
    garden = [item for item in data if not item['is_baby']]
    
    if len(garden) >= 50:
        print("\n[알림] 생명 꽃밭에 비어있는 자리가 없습니다.")
        return

    types = ["총명영특", "무병장수", "부귀영화", "만인덕망", "호연지기"]
    print("\n--- 심을 수 있는 꽃씨의 기운 ---")
    for i, t in enumerate(types, 1):
        count = len([item for item in garden if item['type'] == t])
        print(f"[{i}] {t} (현재 {count}개)")

    try:
        choice = int(input("\n심을 꽃씨의 번호를 선택하세요: "))
        selected_type = types[choice-1]
        
        # 기운별 불균형 예외 처리
        type_count = len([item for item in garden if item['type'] == selected_type])
        if type_count >= 10:
            print(f"\n[알림] {selected_type}의 기운은 충분히 많이 준비했습니다. 다른 기운을 선택해주세요.")
            return

        new_seed = {
            "id": get_next_id(data),
            "type": selected_type,
            "stage": 1,
            "status": "건강",
            "is_baby": False,
            "baby_info": None
        }
        data.append(new_seed)
        save_data(data)
        print(f"\n🌸 새로운 생명의 씨앗({selected_type})을 심었습니다. 현재 정원: {len(garden)+1}개")
    except (ValueError, IndexError):
        print("\n[오류] 올바른 번호를 선택해주세요.")

# 1-2. Read: 조회
def read_garden():
    data = load_data()
    # 꽃밭(is_baby: False)만 필터링
    garden = [item for item in data if not item['is_baby']]
    
    if not garden:
        print("\n[알림] 현재 정원이 비어있습니다.")
        return

    print("\n--- 명진국 꽃밭 둘러보기 ---")
    print("ID | 기운 | 단계 | 상태")
    for f in garden:
        emoji = "🌱" if f['stage'] < 3 else "🌿" if f['stage'] < 5 else "🌸"
        print(f"{f['id']} | {f['type']} | {f['stage']}단계 {emoji} | {f['status']}")

def read_babies():
    data = load_data()
    babies = [item for item in data if item['is_baby']]
    
    if not babies:
        print("\n[알림] 아직 세상에 태어난 아이가 없습니다.")
        return

    print("\n--- 점지한 아이들 명부 ---")
    for b in babies:
        info = b['baby_info']
        spot = "●" if info['mongo_spot'] else "○"
        print(f"ID: {b['id']} | 이름: {info['name']} | 성별: {info['gender']} | 기운: {b['type']} | 반점: {spot}")

# 1-3. Update: 물주기 및 점지
def update_flower():
    data = load_data()
    read_garden()
    try:
        target_id = int(input("\n돌볼 꽃의 ID를 입력하세요: "))
        flower = next((item for item in data if item['id'] == target_id and not item['is_baby']), None)

        if not flower:
            print("\n[오류] 리스트에 존재하지 않는 정보입니다.")
            return

        # 예외 처리: 성장 불가 상태
        if flower['status'] in ["시듦", "과습", "충해"]:
            print(f"\n[알림] {flower['status']} 상태인 꽃에는 물을 줄 수 없습니다.")
            return

        # 물주기 로직
        if flower['stage'] < 5:
            flower['stage'] += 1
            # 확률적 상태 변화
            flower['status'] = random.choices(["건강", "과습", "충해", "시듦"], weights=[70, 10, 10, 10])[0]
            print(f"\n💧 물을 주어 씨앗이 {flower['stage']}단계가 되었고, [{flower['status']}]한 상태가 되었습니다.")
        
        # 상태 전이 (아이 점지)
        if flower['stage'] == 5 and flower['status'] == "건강":
            print("\n✨ 꽃이 만개하여 아이로 탄생할 준비가 되었습니다!")
            name = input("아이의 이름을 지어주세요: ")
            gender = input("아이의 성별을 입력하세요: ")
            
            flower['is_baby'] = True
            flower['baby_info'] = {
                "name": name,
                "gender": gender,
                "mongo_spot": True
            }
            print(f"\n👶 축하합니다! 꽃이 아이({name})로 변신했습니다. 아이를 꽃가마에 태워 세상으로 보내줍니다.")
        
        save_data(data)
    except ValueError:
        print("\n[오류] 숫자 ID를 입력해야 합니다.")

# 1-4. Delete: 시든 꽃 거두기
def delete_flower():
    data = load_data()
    # 생명력을 잃은 꽃만 필터링하여 보여줌
    dead_flowers = [item for item in data if not item['is_baby'] and item['status'] in ["시듦", "과습", "충해"]]
    
    if not dead_flowers:
        print("\n[알림] 현재 거두어야 할 시든 꽃이 없습니다.")
        return

    print("\n--- 거두어야 할 생명들 ---")
    for f in dead_flowers:
        print(f"ID: {f['id']} | 기운: {f['type']} | 상태: {f['status']}")

    try:
        target_id = int(input("\n거둘 꽃의 ID를 입력하세요: "))
        target = next((item for item in data if item['id'] == target_id), None)

        if not target or target['is_baby']:
            print("\n[오류] 올바른 대상이 아닙니다.")
            return

        if target['status'] == "건강":
            print("\n[방지] 건강한 씨앗은 거둘 수 없습니다.")
            return

        confirm = input(f"정말로 {target_id}번 씨앗을 거두시겠습니까? (Y/N): ").upper()
        if confirm == 'Y':
            data.remove(target)
            save_data(data)
            print("\n🥀 삼신할매가 생명을 거두어 품으로 안았습니다. 다음 생에는 더 튼튼하게 태어날 것입니다.")
    except ValueError:
        print("\n[오류] 올바른 번호를 입력하세요.")

# 메인 루프
def main():
    while True:
        print("\n" + "="*40)
        print("      🌸 삼신할매의 생명 정원 🌸")
        print("="*40)
        print("1. 꽃씨 심기 (Create)")
        print("2. 꽃밭 둘러보기 (Read)")
        print("3. 정원 돌보기/물주기 (Update)")
        print("4. 점지한 아이들 확인 (Read)")
        print("5. 시든 꽃 정리 (Delete)")
        print("0. 종료")
        print("="*40)
        
        choice = input("선택: ")
        if choice == '1': create_seed()
        elif choice == '2': read_garden()
        elif choice == '3': update_flower()
        elif choice == '4': read_babies()
        elif choice == '5': delete_flower()
        elif choice == '0': break
        else: print("\n[알림] 잘못된 선택입니다.")

if __name__ == "__main__":
    main()
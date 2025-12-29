import json
import os

# 1. 파일 경로 설정 (상대 경로 활용)
# json 폴더 안에 있는 파일들에 접근하기 위한 경로 문자열입니다.
GONG_PATH = "json/gong.json"
TO_BE_SANTA_PATH = "json/tobesanta.json"

def initialize_game():
    """게임을 초기화하며 gong.json을 복사하여 tobesanta.json을 생성하는 함수"""
    
    # [Read] 먼저 gong.json 파일을 읽어옵니다.
    # 'r'은 읽기(Read) 모드, encoding은 한글 깨짐 방지를 위해 설정합니다.
    with open(GONG_PATH, 'r', encoding='utf-8') as f:
        gong_data = json.load(f) # 파일의 내용을 파이썬 딕셔너리로 변환합니다.
        
    # [Create] 읽어온 데이터를 tobesanta.json이라는 이름으로 저장합니다.
    # 'w'는 쓰기(Write) 모드입니다. 파일이 없으면 새로 생성합니다.
    with open(TO_BE_SANTA_PATH, 'w', encoding='utf-8') as f:
        # indent=4는 가독성을 위해 들여쓰기를 적용하는 옵션입니다.
        json.dump(gong_data, f, ensure_ascii=False, indent=4)
        
    print("--- 시스템: tobesanta.json 파일 생성 완료 ---")
    
    # 제대로 연결됐는지 확인하기 위해 데이터를 다시 읽어서 출력해봅니다.
    with open(TO_BE_SANTA_PATH, 'r', encoding='utf-8') as f:
        check_data = json.load(f)
        print("불러온 데이터 확인:", check_data["status"]["clothes"]["outer"])

# 함수 실행
if __name__ == "__main__":
    initialize_game()
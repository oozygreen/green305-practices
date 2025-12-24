import time
import sys

# [Scenario] 대용량 커피 원두 데이터 처리 (배열 + 반복 + 조건)
# 목표: 로스팅 날짜가 7일 이내이고, 평점이 4.5 이상인 원두 필터링

# 1. 더미 데이터 생성 (100만 개) - 메모리 부하 테스트
coffee_beans = [
    {"id": i, "roast_days": i % 30, "score": (i % 50) / 10} 
    for i in range(1000000)
]

print(f"Dataset Size: {sys.getsizeof(coffee_beans) / (1024*1024):.2f} MB")

# ---------------------------------------------------------
# ❌ [Bad Practice] : Python의 느린 For loop + 중첩 If
# ---------------------------------------------------------
start_time = time.time()
selected_beans = []
for bean in coffee_beans:
    # 파이썬 인터프리터가 매번 타입 체크와 속성 조회를 수행 (오버헤드 발생)
    if bean["roast_days"] <= 7:
        if bean["score"] >= 4.5:
            selected_beans.append(bean)
end_time = time.time()
print(f"Bad Loop Time: {end_time - start_time:.4f} sec")

# ---------------------------------------------------------
# ✅ [Best Practice 1] : List Comprehension (Pythonic)
# ---------------------------------------------------------
# 파이썬 내부 C언어 루틴으로 최적화되어 속도가 훨씬 빠름
start_time = time.time()
# Short-circuit logic: score >= 4.5 조건이 더 희소하다면 먼저 검사하는 게 빠를 수 있음 (데이터 분포에 따라 다름)
selected_beans_v2 = [
    bean for bean in coffee_beans 
    if bean["roast_days"] <= 7 and bean["score"] >= 4.5
]
end_time = time.time()
print(f"List Comp Time: {end_time - start_time:.4f} sec")

# ---------------------------------------------------------
# 🚀 [Architect's Insight] : Generator Expression (Memory Efficient)
# ---------------------------------------------------------
# 100만 개 중 조건 맞는 게 50만 개라면, 그걸 다 리스트로 만드는 것도 메모리 낭비.
# 필요할 때 하나씩 꺼내 쓰는 'Generator' 사용.
selected_beans_gen = (
    bean for bean in coffee_beans 
    if bean["roast_days"] <= 7 and bean["score"] >= 4.5
)
# print(next(selected_beans_gen)) # 필요할 때 소비
print(f"Generator Size: {sys.getsizeof(selected_beans_gen)} Bytes (매우 작음!)")

# [Lesson]
# 1. 대용량 처리에서는 '어떻게 반복하느냐'가 성능을 좌우함.
# 2. If문의 순서도 데이터 분포에 따라 성능에 영향을 미침.
# 3. 메모리가 부족할 땐 List 대신 Generator를 고려해야 함.
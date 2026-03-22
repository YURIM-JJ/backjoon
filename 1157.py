N = input().upper()  
# 입력 문자열을 받아서 모두 대문자로 변환
# → 대소문자 구분 없이 처리하기 위함

cnt = [0] * 26  
# 알파벳 A~Z의 개수를 저장할 리스트 생성 (총 26칸)
# cnt[0] → 'A', cnt[1] → 'B', ... cnt[25] → 'Z'

for ch in N:  
    # 문자열을 한 글자씩 순회

    idx = ord(ch) - ord('A')  
    # 문자를 숫자로 변환하여 인덱스로 사용
    # 예:
    # 'A' → 65 → 65 - 65 = 0
    # 'B' → 66 → 66 - 65 = 1
    # 'Z' → 90 → 90 - 65 = 25

    cnt[idx] += 1  
    # 해당 알파벳 위치의 개수를 1 증가

max_cnt = max(cnt)  
# 가장 많이 등장한 알파벳의 개수

# 최댓값이 여러 개면 ? 출력
if cnt.count(max_cnt) > 1:  
    # cnt 리스트에서 최댓값이 2개 이상이면
    print('?')  
    # 가장 많이 사용된 알파벳이 여러 개 → 문제 조건상 '?' 출력

else:
    idx = cnt.index(max_cnt)  
    # 최댓값이 처음 등장하는 위치(인덱스) 찾기
    # → 가장 많이 나온 알파벳의 위치

    print(chr(idx + ord('A')))  
    # 인덱스를 다시 문자로 변환
    # 예:
    # idx = 0 → chr(65) → 'A'
    # idx = 2 → chr(67) → 'C'

# ====================================

# 1. 입력받고 대문자로 통일 (대소문자 구분 제거)
N = input().upper()

# 2. 문자별 개수를 저장할 딕셔너리 생성
# key: 문자, value: 등장 횟수
cnt = {}

# 3. 문자열을 하나씩 순회하면서 개수 세기
for ch in N:
    # dict.get(key, 기본값)
    # → key가 있으면 value 반환
    # → 없으면 기본값 반환
    # 여기서는 없으면 0으로 시작
    cnt[ch] = cnt.get(ch, 0) + 1

# 예시:
# "MISSISSIPI" → {'M':1, 'I':4, 'S':4, 'P':1}

# 4. 등장 횟수 중 최댓값 찾기
# dict.values() → value들만 모은 리스트 같은 객체
max_cnt = max(cnt.values())

# 5. 최댓값을 가진 문자들 찾기
# dict.items() → (key, value) 쌍으로 가져옴
# 예: ('A', 3), ('B', 2)
candidates = []

for k, v in cnt.items():
    if v == max_cnt:
        candidates.append(k)

# 6. 결과 출력
# 최댓값이 여러 개면 '?' 출력
if len(candidates) > 1:
    print('?')
else:
    print(candidates[0])
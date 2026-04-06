# 🌸 대자연의 스케줄러
## 봄꽃 개화 릴레이와 데이터 정렬 알고리즘

**학번**: 20234300, 20234285  
**이름**: 김규일 · 이서진 · 박효림

---

## 1. 시작하며
봄이 오면 산과 들은 색색의 꽃으로 물듭니다. 하지만 모든 꽃이 같은 날 피지는 않습니다. 매화가 먼저 봄을 알리고, 개나리가 뒤따르며 진달래와 벚꽃이 차례로 만개합니다.

프로그래머의 시선으로 보면, 자연은 꽃의 개화 순서를 관리하기 위해 **데이터 구조화(Data Structuring)**와 **정렬(Sorting) 알고리즘**을 사용하는 것처럼 보입니다.

---

## 2. 개화 릴레이의 단계적 분해
봄꽃의 개화 과정은 다음과 같은 4단계로 나눌 수 있습니다.

1. **데이터 초기화 (겨울)**  
   모든 꽃눈이 개화 조건을 가진 채 대기 상태 유지
2. **순서 정렬 (초봄)**  
   개화 적정 온도를 기준으로 오름차순 정렬
3. **순차 탐색 (봄 진행)**  
   기온 상승에 따라 조건 충족 여부 탐색
4. **상태 변화 (만개)**  
   조건 충족 시 상태를 `대기 → 개화`로 변경

---

## 3. 꽃 데이터의 추상화 및 구조화
복잡한 자연 현상을 단순화하여 Python의 `dict` 구조로 표현했습니다.

| Key | Type | Description |
| --- | --- | --- |
| `name` | `str` | 꽃 이름 |
| `target_temp` | `int` | 개화 적정 온도 |
| `is_bloomed` | `bool` | 개화 여부 |

---

## 4. 릴레이 개화 알고리즘 (Python)
```python
# 1. 데이터 구조화
flowers = [
    {"name": "매화", "target_temp": 5,  "is_bloomed": False},
    {"name": "수선화", "target_temp": 9,  "is_bloomed": False},
    {"name": "개나리", "target_temp": 10, "is_bloomed": False},
    {"name": "튤립", "target_temp": 11, "is_bloomed": False},
    {"name": "진달래", "target_temp": 12, "is_bloomed": False},
    {"name": "목련", "target_temp": 13, "is_bloomed": False},
    {"name": "라일락", "target_temp": 14, "is_bloomed": False},
    {"name": "벚꽃", "target_temp": 15, "is_bloomed": False},
]

# 2. 정렬
flowers.sort(key=lambda x: x['target_temp'])

# 3. 기온 상승 시뮬레이션
current_temp = 0
while current_temp <= 15:
    current_temp += 1
    for flower in flowers:
        if not flower['is_bloomed'] and current_temp >= flower['target_temp']:
            flower['is_bloomed'] = True
            print(f"[기온 {current_temp}°C] {flower['name']} 개화")
```

---

## 5. 컴퓨팅 사고 요소
- **데이터 구조화**: List와 Dictionary로 정보 체계화
- **정렬 알고리즘**: 기준에 따른 순서 결정
- **상태 제어**: Boolean 값으로 중복 개화 방지

---

## 6. 마치며
자연의 봄꽃 개화 순서는 무작위가 아니라, 명확한 조건과 순서에 따라 동작하는 하나의 알고리즘처럼 보입니다.

이번 과제를 통해 컴퓨팅 사고는 단순한 코딩 기술이 아니라, 세상을 논리적으로 해석하고 모델링하는 사고 방식임을 배웠습니다.

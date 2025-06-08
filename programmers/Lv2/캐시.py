# 프로그래머스 - Lv2 - 캐시 - 자료구조(큐), LRU 캐시, 구현 문제
"""
자료구조(큐), LRU 캐시, 구현 문제

[핵심 아이디어]
    1. LRU(Least Recently Used) 캐시 알고리즘을 deque로 구현한다.
    2. 캐시 히트 시 해당 원소를 제거 후 맨 뒤로 이동시켜 최근 사용으로 업데이트한다.
    3. 캐시 미스 시 캐시 크기가 가득 찬 경우 가장 오래된 원소(맨 앞)를 제거하고 새 원소를 맨 뒤에 추가한다.
    4. 대소문자 구분을 하지 않으므로 모든 도시명을 소문자로 변환하여 처리한다.

[풀이 과정]
    1. 각 도시를 순차적으로 처리하며 소문자로 변환한다.
    2. 캐시에 해당 도시가 존재하는 경우 (cache hit):
       - 실행시간에 1을 추가한다.
       - 해당 도시를 캐시에서 제거 후 맨 뒤에 다시 추가하여 최근 사용으로 표시한다.
    3. 캐시에 해당 도시가 존재하지 않는 경우 (cache miss):
       - 실행시간에 5를 추가한다.
       - 캐시 크기가 0이 아닌 경우, 캐시가 가득 차면 맨 앞 원소를 제거한다.
       - 새 도시를 캐시 맨 뒤에 추가한다.
    4. 캐시 크기가 0인 경우 모든 요청이 cache miss가 되어 항상 실행시간 5가 추가된다.
"""

from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque()

    for city in cities:
        city = city.lower()  # 대소문자 구분 없이 처리

        if city in cache:  # cache hit
            answer += 1
            cache.remove(city)  # 기존 위치에서 제거
            cache.append(city)  # 맨 뒤로 이동 (최근 사용으로 업데이트)
        else:  # cache miss
            answer += 5
            if cacheSize != 0:  # 캐시 크기가 0이 아닌 경우만 캐시 사용
                if len(cache) >= cacheSize:  # 캐시가 가득 찬 경우
                    cache.popleft()  # 가장 오래된 원소(LRU) 제거
                cache.append(city)  # 새 도시를 맨 뒤에 추가

    return answer

cities = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']
print(solution(3, cities))  # 50

cities = ['Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul']
print(solution(3, cities))  # 21

cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
print(solution(2, cities))  # 60

cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
print(solution(5, cities))  # 52

print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))  # 16
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))  # 25

# 모의고사
* 입력 : 수학 과목 정답 리스트 `answers`
* 출력 : 수포자 중 가장 많이 맞힌 사람 리스트

* 수포자 1, 2, 3은 문제를 찍을 때 본인의 패던으로 찍는다.
* 가장 많이 맞힌 사람이 2명 이상일 때 오름차순으로 정렬하여 리턴한다.


## mine
* 각 수포자의 패턴을 리스트로 저장
* 각 수포자별로 몇 문제 맞췄는지 확인
    - `index % len(pattern)`을 통해 순환하여 접근
* 만약 가장 많이 맞힌 사람이 없다면
    - 가장 첫 수포자, `answer` 리스트가 비어있음
    - `answer` 리스트에 추가
* `answer` 리스트에 있다면
    - 가장 많이 맞힌 갯수 `max_score`를 구한 후,
    - `max_score` 보다 점수가 많다면
        - `answer` 리스트 초기화 후 정보 추가
    - `max_score`와 동일하다면
        - 그냥 정보 추가


## 멋진 코드 #1
* 수포자별로 점수를 계산한 내 방식과는 다르게 각 문항을 맞췄는지 길이가 3인 리스트 `score`에 저장한다.
    - 수포자 -> 문항의 접근이 아닌 문항 -> 수포자
- 이후 `score`의 최댓값과 동일한 수포자의 아이디를 정답 배열에 저장한다.
* 직관적이고 간결하다.

## 멋진 코드 #2
* 멋진 코드 #1과 동일하다.
* 더 간결하게 적힌 듯 하다.

---------
## 오늘의 교훈
~~~
천천히 짜자,,
문제 하나 푸는데 시간이 오래 걸려서 마음이 급하다.
그리고 한 부분을 구현하면서 다른 부분은 어떻게 구현할지 생각하게 되는데,
지금 하고 있는 부분도 헷갈리게 돼서 좋지 않은 것 같다.
~~~
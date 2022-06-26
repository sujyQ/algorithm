# H-index
* 입력 : 논문 인용 횟수 리스트 `citations`
* 출력 : H-index

* 논문 `n`편 중 `h`번 이상 인용된 논문이 `h`개 이상일 때 H-index는 `h`의 최댓값이 됨

## mine
* 의도
    - 내림차순 정렬로 높은 인용수부터 0까지 줄어들며 확인
    - `sorted_cit`중 `i`보다 같거나 큰 인용수가 몇 개 있는지 확인
    - `_cits`의 합이 `i`보다 같다면
    - `i` 이상 인용된 논문이 `i` 이상인 것
    - `for - for`구조여서 오래 걸릴 듯 하고 `_cits`를 구하는게 맘에 안든다.
        - 이걸 신경써서 오름차순으로 하긴 했지만,,,


## 멋진 코드 #1
* H-index 후보 구하기
    - `enumerate(citations, start=1)`으로 `(index, citation)` 형태로 묶기, `index`는 1부터 시작
    - `map(min, enumerate(citations, start=1))`으로 H-index 후보를 구한다
* 구한 H-index 후보들 중 `max()`로 최댓값을 구한다

+ 근데 아직 `map(min, enumerate(citations, start=1))`이 왜 H-index 후보가 되는지 모르겠다.

## 멋진 코드 #2
* `citations`를 오름차순 정렬
    - 가장 작은 인용 횟수부터 시작
    - 논문이 몇 편이 남았는지 (`l-i`), 그리고 남은 논문이 모두 현재 인용 횟수보다 많이 인용되었는지? 의 사고


## 멋진 코드 #3
* `filter`를 통해 `l`의 원소 중 주어진 조건 (`lambda x : x >= n`)을 만족하는 원소를 찾음
    - `filter(func, iterable)` : 여러 개의 데이터로부터 일부만 추출할 때 사용
        - `func` : 일반 함수, 람다 함수 등등
        - `filter object`를 리턴해서 `list()` 혹은 `tuple()`의 작업이 필요하다


---
## 오늘의 얻음
~~~
문제에 주어진 조건을 반대로 생각하면 간단하게 구현할 수 있다!
~~~

~~~python
# list l에 n보다 큰 원소 구하기
list(filter(lambda x: x >= n, l))
~~~

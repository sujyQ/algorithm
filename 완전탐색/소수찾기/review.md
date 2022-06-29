# 소수찾기
* 입력 : 한자리 숫자 (0~9)가 담긴 종이 조각 `numbers`
* 출력 : 종이 조각으로 만들 수 있는 소수

* `011`은 `11`과 동일하다

## mine
* `itertools`의 `permutations`를 가지고 구할 수 있는 모든 조합을 구함
* `getInt(num_ch)`로 문자열을 정수형으로 변경, `permutation_list`에 입력
*  `permutation_list`의 원소를 하나씩 꺼내면서
    - 정답 리스트 `answer_list`에 이미 있다면 패스
    - 없는데 소수라면 정답 리스트에 추가

* 단점 : 소수가 아니라면 정답 리스트에 들어있지 않으므로 소수가 아닌 수는 여러번 소수인지 검사하게 된다.

## 멋진 코드 #1
* 문자열 합치기
    - `"".join(list)`를 하면 `list`로 들어온 문자들을 하나로 합친다.
    - e.g., `"".join(['s','u','j','y']) -> "sujy"`
    - `map(int, string)`으로 정수형으로 타입 캐스팅

* 중복되는 값 제거하기
    - `set` 이용 : 순서가 없으며 unique한 값을 갖는다
    - 연산자 `|=`는 합집합을 의미

* 소수 구하기
    - 0과 1은 소수가 아니므로 범위에서 제외
    - 어떤 수 `n`의 약수는 무조건 `sqrt(n)` 이하의 값이다.
        - 범위를 `range(2, sqrt(n)+1)`로 설정
    - `i`의 배수가 되는 수가 있다면 `set`에서 제외
        - 차집합 연산
    - `set`에 남아있는 수가 소수가 된다.

## 멋진 코드 #2
* 조합 구하기
    - `makeCombinations(str1, str2)`라는 재귀함수로 가능한 조합을 구한다.
    - `str1`에 `str2[i]`를 더해가면서 함수를 호출
    - 처음으로 다시 호출된 함수에서는 한 글자씩 더해지고
        - 그 다음으로 호출된 함수에서는 두 글자가 더해지는 방식
        - 계속 반복, `str2`의 길이만큼 `for`문이 반복되면 종료됨
    - `str1`은 생성된 조합이고 `str2`는 더해질 숫자들

## 오늘의 얻음
~~~python
some_set = set()
another_set = set()
some_set |= another_set
some_set -= another_set
some_set.add(something)
~~~

~~~python
def makeCombinations(str1, str2):
    for i in range(len(str2)):
        makeCombinations(str1 + str2[i], str2[:i] + str2[i + 1:])

makeCombinations("", "123")
~~~

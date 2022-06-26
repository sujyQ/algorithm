# 가장 큰 수
입력 : 0 또는 양의 정수가 담긴 배열 `numbers`
출력 : `numbers`의 정수들을 이어붙여 만들 수 있는 최대 정수

* `numbers` 원소는 0 이상 1000 이하
* 문자열로 바꾸어 반환

## mine
* 계획
    - `numbers`를 모두 문자열로 바꾼 후 정렬하기
        - 문자열 정렬은 숫자 정렬과 다르게 앞 글자부터 비교한다.
    - 비교 후 앞 숫자가 같은 경우 그 다음 숫자를 비교한다
        - e.g. `[30, 3] -> "330"`이 되도록

* 에러사항
    - `[0, 0, 0, 0]`이 입력됐을 때 `"0000"`이 출력된다.
    - `[10, 101]`의 경우 `"10110"`이 아닌 `"10101"`이 출력된다.
    - 결국 공개된 테스트 케이스만 통과하는 로직

## 멋진 코드 #1
* 크기 비교를 위해 `str(number)*4`
    - `numbers`의 원소를 4번 반복하여 자릿수 차이를 해결
    - 이후 반복한 문자열에서 자릿수만큼 `split`
    - `[0, 0, 0, 0]`과 같이 모두 `0`이 들어왔을 때 0이 출력되도록 `sum_` 사용
        - `if sum_ == 0 :` 구문을 `for`안에 넣지 않고
        - `for`문 시작하기 전에, 정렬이 된 `tmp`의 맨 처음이 0이면 `return '0'`을 해도 되지 않을까

## 멋진 코드 #2
* `def comparator`를 `functools.com_to_key`로 사용
    - `funcfools`에는 효율적인 메서드가 많은 것 같다. `functools.partial`도 그렇구,,
    - `sorted()`에서 `key`를 통해 정렬기준을 지정할 수 있다. `lambda`를 쓰는건 많이 봤는데
        - `functools.com_to_key()`는 `key`에 함수를 지정할 때 사용된다.
        - `lambda`를 쓰는 것과 비슷
        - 두 개의 인수를 입력받아 첫 번째 인수가 더 크면 양수, 같으면 0, 더 작으면 음수를 반환
    
* 참고 사이트 
- [sorting HOWTO] (https://docs.python.org/ko/3/howto/sorting.html#sortinghowto)
- [functools] (https://docs.python.org/ko/3/library/functools.html)


------
## 오늘의 얻음
~~~python
import functools

def comparator(a, b)
    if a > b :
        return 1

    elif a < b :
        return 0

    else :
        return -1

_sorted = sorted(target, ket=functools.com_to_key(comparator))
~~~
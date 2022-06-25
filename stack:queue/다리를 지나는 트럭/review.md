# 다리를 지나는 트럭
입력 : 다리의 길이 `bridge_length`, 다리가 버틸 수 있는 최대 무게 `weight`, 대기중인 트럭의 무게 `truck_weights`    
출력 : 대기중인 트럭이 모두 다리를 건널 때 까지 걸리는 시간(초)

* 다리 위에 있는 트럭은 1초에 1씩 전진
* 다리 위의 트럭 무게는 `weight`보다 클 수 없음
* 다리 위의 트럭은 `bridge_length`보다 많을 수 없음

## mine
* 의도
    - 시간을 담는 `seonds`를 1씩 증가시키면서 `while`이 끝났을 때 총 흘러간 시간을 알 수 있도록
    - `truck_weights`에 있는 트럭을 `on_bridge`에 `enqueue`
        - `going`에 트럭이 얼마나 전진했는지 저장
        -  맨 앞 요소가 `bridge_length`만큼 전진했다면 `dequeue`
    - 다리에 자리가 남아있고 여유 무게도 있다면
        - 조건 확인 후 `going`과 `on_bridge`에 `enqueue`
    - `while` 종료 조건 : 남은 트럭도 없고 다리 위에도 트럭이 없을 때

* 단점
    - `sum(on_bridge)` 때문에 다리 길이가 길수록, 다리 위에 트럭이 많이 있을수록 오래 걸린다.
        - 어떤 케이스에서는 실행 시간이 100ms를 넘기도 했다.


## 멋진 코드 #1
* `class Bridge()`로 다리 클래스 사용
    - `def push(self, truck)` : 다리에 트럭이 더 올리기
        - 가능하다면 트력을 더 올리고 True 리턴
        - 불가능하면 False 리턴
    - `def pop(self)` : 다리를 다 건넌 트럭 제거하기
        - `self._current_weight`에서 해당 무게를 뺌
        - `sum()` 사용하지 않고도 다리 위의 무게를 구할 수 있다.

--------

## 오늘의 얻음
~~~
제발 주어진 예제로 시뮬레이션 하면서 계획을 세우자.
무턱대고 코드 먼저 적기 금지.
~~~


~~~python
if any(p < k for p, k in zip(p_list, k_list))
if all(p < k for p, k in zip(p_list, k_list))
~~~


~~~python
# sum() 사용하지 않기

total = 0 
...
total += weight
...
total -= weight
~~~

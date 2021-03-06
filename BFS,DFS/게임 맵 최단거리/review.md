# 게임 맵 최단거리
* 입력 : 게임 맵 `maps`
* 출력 : 최단 이동 거리

* 시작은 항상 `(0,0)`에서 한다
* 상대 팀 진영은 항상 `(n,m)`에 있다. (`n`x`m` 크기의 맵)
* `maps`는 `1` 또는 `0`으로 이루어져 있다.
    - `1` : 이동 가능
    - `0` : 벽으로 막혀있어 이동 불가능
* 상대 팀 진영이 벽으로 둘러쌓여있어 진입이 불가능한 경우 `-1`을 리턴한다.



## mine #1
* 정확성, 효율성 모두 통과하지 못했다
* 의도
    - DFS로 상대 팀 진영에 도달하는 경우의 수를 구한 후,
    - 최단 경로를 구함
* 미궁에서 DFS를 사용하는 것은 연산량이 매우 크고 당연히 시간 복잡도 또한 크다 ([참고](https://school.programmers.co.kr/questions/18867))


## mine #2
* 위의 [참고](https://school.programmers.co.kr/questions/18867) 사이트의 설명을 보고 BFS 방식으로 구현, 테스트 통과
* 지뢰찾기처럼 현재 위치에서 갈 수 있는 곳을 파악하고 거리를 저장
* 현재 위치에서 이동할 수 있는 위치를 `queue`에 삽입
    - 맵을 벗어나지 않고
    - 벽으로 막혀있지 않으며
    - 방문한 적이 없는 위치
* `queue`에 삽입한 위치를 방문처리함
    - 방문을 저장하는 `visited`에 거리를 저장
* 모든 탐색이 끝난 후, 상대 팀 진영 위치에 해당하는 부분이 0이라면
    - 벽에 둘러쌓여있어 진입이 불가능한 경우, `-1` 리턴
    - 아니면 거리 `visited[-1][-1]`을 리턴


## 멋진 코드
* BFS, 현재 위치에서 갈 수 있는 곳을 파악하고 거리를 저장하는 것은 동일
* 다른 점 :
    - 현재 위치가 상대 팀 진영 위치라면 중간에 이동 거리를 반환한다.
    - 시작 이동 거리 `d`가 `1`이며 거리를 저장할 때 `d+1`을 저장한다.


## 배운 점
~~~
탐색을 할 때, 방문 처리를 해야 `maximum depth recursion` 에러가 나지 않는다.
~~~

~~~
미궁에서 최단 경로를 구할 때에는 BFS를 쓰는 것이 효율적이다.
현재 위치에서 갈 수 있는 길이 3가지가 되는 경우가 많을수록 DFS는 불리하다.
~~~
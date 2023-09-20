### 찐 사수와 같이 하는 알고리즘([사용법](./refer/README.md))
- [visual with code](https://swexpertacademy.com/main/visualcode/main.do)
- 코딩테스트 문제를 풀며 알고리즘  [refer link](https://youtube.com/playlist?list=PLRx0vPvlEmdDHxCvAQS1_6XV4deOwfVrz)
[빅오(Big-O)표기법 완전정복](https://youtu.be/6Iq5iMCVsXA)

### 주요 참조 
+ [Trees & Graphs](https://youtube.com/playlist?list=PLjSkJdbr_gFY8VgactUs6_Jc9Ke8cPzZP)

### 종류별 알고리즘 hint
+ 그리디 : 뒤에서 부터 해 보기 - [이코테 2021](https://youtu.be/2zjoKjt97vQ)
+ 보통 깊이 우선 탐색 : 함수안에서 주로 재귀
+ 넓이 우선 탐색 : 큐나 데크에 저장 후 반복해 찾음.

<details open>
<summary>종류별 알고리즘</summary>

| 분류 | 제목 | 설명 | 시간복잡도 | 기본의미 | 풀기 | function | 연관 |
| :---: | --- | :---: | :---: | :---: | :---: | :---: | :---: |
|정렬|[선택 정렬(Selection Sort)](https://youtu.be/8ZiSzteFRYc)|기준 값과 반복 비교해 앞으로 보냄|$O(N^2)$|[doc](https://docs.google.com/spreadsheets/d/18TZ_dfJ_MY6-XAnB3lV5-C2skDgVgrPZkPTDCbKVpF4/edit#gid=0)|[yet](https://www.acmicpc.net/problem/2750)|-|[link](https://youtu.be/V_RcpaHcULM)| 
|정렬|[버블 정렬(Bubble Sort)](https://youtu.be/EZN0Irp2aPs)|옆 값과 비교해 앞으로 보냄 반복|$O(N^2)$|[doc](https://docs.google.com/spreadsheets/d/18TZ_dfJ_MY6-XAnB3lV5-C2skDgVgrPZkPTDCbKVpF4/edit#gid=2018194806)|[yet](https://www.acmicpc.net/problem/2752)|-|[link](https://youtu.be/V_RcpaHcULM)| 
|정렬|삽입 정렬(Insertion Sort)|비교 대상 값들 사이에 크기로 위치|$O(N^2)$||-|-|[link](https://youtu.be/16I9Z7bS1iM)| 
|정렬|[퀵 정렬(Quick Sort)](https://youtu.be/7BDzle2n47c)|정한 값 기준 분할해 작은/큰 값으로 위치 반복, 가장 많이 사용|$O(N^2)$~$O(N*log_2N)$|[doc](https://docs.google.com/spreadsheets/d/18TZ_dfJ_MY6-XAnB3lV5-C2skDgVgrPZkPTDCbKVpF4/edit#gid=730421551)|?|-|[link](https://youtu.be/V_RcpaHcULM)| 
|정렬|병합정렬(Merge Sort)|두 단위로 쪼개어 비교 후 반복 비교해 붙임, 임시 메모리 공간 필요|$O(N*log_2N)$|[doc](https://docs.google.com/spreadsheets/d/18TZ_dfJ_MY6-XAnB3lV5-C2skDgVgrPZkPTDCbKVpF4/edit#gid=1410825905)|-|-|| 
|정렬|힙정렬(Binary Heaps)|완전이진트리 기반 구조,우수하나 특별한 상황 사용|$O(log_2N)$|[diagrams](https://app.diagrams.net/#G16oevZ5ILcp0nb1a_AIiogbryfRILW0q_)|-|-|[link](https://youtu.be/jfwjyJvbbBI)|  
|정렬|계수정렬(Counting Sort)|제한된 값 이하 때 사용, 반복 값 많을 때 유리|$O(N)$|[doc](https://docs.google.com/spreadsheets/d/18TZ_dfJ_MY6-XAnB3lV5-C2skDgVgrPZkPTDCbKVpF4/edit#gid=67632374)|[yet](https://www.acmicpc.net/problem/10989)|-|[link](https://youtu.be/n4kbFRn2z9M)|  
|Graph|깊이 우선 탐색(Deepth First Search)|||[drawio](https://app.diagrams.net/#G16oevZ5ILcp0nb1a_AIiogbryfRILW0q_)|-|-|[link](https://youtu.be/_hxFgg7TLZQ)| 
|Graph|너비 우선 탐색(Breath First Search)|||[drawio](https://app.diagrams.net/#G16oevZ5ILcp0nb1a_AIiogbryfRILW0q_)||-|[link](https://youtu.be/2zjoKjt97vQ)| 
|그리디|루트로 시작, 레벨 순으로 왼쪽, 오른쪽 끝 순으로 반복||큐사용||-|-|[link](https://youtu.be/2zjoKjt97vQ)| 
|MST|Kruskal Minimum Spanning Tree||greedy method||-|[py](./python/MinimumSpanningTree_Kruskal.py)|| 
 
</details>

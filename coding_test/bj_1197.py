'''
문제
그래프가 주어졌을 때, 그 그래프의 최소 스패닝 트리를 구하는 프로그램을 작성하시오.

최소 스패닝 트리는, 주어진 그래프의 모든 정점들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리를 말한다.

입력
첫째 줄에 정점의 개수 V(1 ≤ V ≤ 10,000)와 간선의 개수 E(1 ≤ E ≤ 100,000)가 주어진다. 다음 E개의 줄에는 각 간선에 대한 정보를 나타내는 세 정수 A, B, C가 주어진다. 이는 A번 정점과 B번 정점이 가중치 C인 간선으로 연결되어 있다는 의미이다. C는 음수일 수도 있으며, 절댓값이 1,000,000을 넘지 않는다.

그래프의 정점은 1번부터 V번까지 번호가 매겨져 있고, 임의의 두 정점 사이에 경로가 있다. 최소 스패닝 트리의 가중치가 -2,147,483,648보다 크거나 같고, 2,147,483,647보다 작거나 같은 데이터만 입력으로 주어진다.

출력
첫째 줄에 최소 스패닝 트리의 가중치를 출력한다.
'''
# 최소신장트리

V,E = map(int, input().split())

costs = []
for i in range(E):
    costs.append(tuple(map(int, input().split())))

costs.sort(key= lambda x: x[2]) # 가중치가 낮은 순서로 정렬

answer = 0 # 가중치의 합의 최소
connect = set([costs[0][0]]) 
# 최소 신장 트리의 첫 원소로 가중치가 가장 낮은 노드 추가

while len(connect) != V: # 최소 신장 트리의 원소가 노드의 총 개수가 될 때까지
    for cost in costs:
        if cost[0] in connect and cost[1] in connect: # 두 원소 모두 이미 트리에 포함되있으면 스킵
            continue
        if cost[0] in connect or cost[1] in connect: # 둘중 하나만 포함되어 있을 경우
            connect.update([cost[0], cost[1]]) # 신장 트리에 추가
            answer += cost[2] # 가중치를 더해줌
            break # for문을 초기화 후 다시 돌림
print(answer)
print(connect)
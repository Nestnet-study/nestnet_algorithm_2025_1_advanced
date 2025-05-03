#include <cstdio>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

// u: 간선의 출발점의 좌표 인덱스
// v: 간선의 도착점의 좌표 인덱스
// dist: 간선의 길이
struct Edge {
	int u;
	int v;
	double dist;
};

bool greaterDist(Edge, Edge);

int n, m;
int x[1000], y[1000];
vector<Edge> edge;
int vertex[1000];

int main() {
	scanf("%d %d", &n, &m);

	// 각 노드의 좌표 입력
	for (int i = 0; i < n; i++) {
		scanf("%d %d", &x[i], &y[i]);
	}
	// 연결된 노드 쌍 입력
	for (int i = 0; i < m; i++) {
		int mx, my;
		scanf("%d %d", &mx, &my);
		mx--; my--;
		// u < v 성립하도록 할당하기
		if (mx < my)
			edge.push_back({ mx, my, 0 });
		else
			edge.push_back({ my, mx, 0 });

	}
	sort(edge.begin(), edge.end(), greaterDist);
	
	// 거리 정보 저장 - 무방향 그래프니까 u < v인 경우만 저장
	int m_index = 0;
	for (int i = 0; i < n; i++) {
		for (int j = i + 1; j < n; j++) {
			// 이미 연결되었는지 검사
			if (m_index < m && edge[m_index].u == i && edge[m_index].v == j) {
				m_index++;
				continue;
			}

			long long dx = x[i] - x[j];
			long long dy = y[i] - y[j];
			edge.push_back({ i, j, sqrt(dx * dx + dy * dy) });
		}
	}

	// 거리에 따라 오름차순으로 정렬
	sort(edge.begin(), edge.end(), greaterDist);

	// 크루스칼 알고리즘
	double ans = 0;
	for (int i = 0; i < n; i++)
		vertex[i] = i;
	for (int i = 0; i < edge.size(); i++) {
		if (vertex[edge[i].u] != vertex[edge[i].v]) {
			ans += edge[i].dist;

			int set = vertex[edge[i].v];
			for (int j = 0; j < n; j++)
				if (vertex[j] == set)
					vertex[j] = vertex[edge[i].u];
		}
	}

	printf("%.2lf\n", ans);
}

bool greaterDist(Edge e1, Edge e2) {
	if (e1.dist == e2.dist) {
		if (e1.u == e2.u)
			return e1.v < e1.v;
		else
			return e1.u < e2.u;
	}
	else
		return e1.dist < e2.dist;
}
#include<iostream>
#include<vector>
#include<queue>
#define INF 100000000

using namespace std;

typedef pair<int, int> ci;
struct info {
	int a;
	int b;
	int t;
};

vector<int>dist;
int n, m;
int a, b, t;
vector<info>lists;
int graphs[1001][1001] = { {0,} };

vector<int>before;

int dijkstra() {


	dist[1] = 0;
	priority_queue<ci, vector<ci>, greater<>>pq;
	pq.push({ 0,1 });

	while (!pq.empty()) {

		int w = pq.top().first;
		int e = pq.top().second;
		pq.pop();

		if (dist[e] < w)continue;

		for (int i = 1; i <= n; i++) {
			if (i == e)continue;
			int ne = i;
			int nw = graphs[e][ne];
			//cout << e << ' ' << ne << ' ' << nw << '\n';
			if (nw == 0)continue;
			if (dist[ne] > (w + nw)) {
				before[ne] = e;
				dist[ne] = w + nw;
				pq.push({ dist[ne],ne });
			}
		}
	}

	return dist[n];
}

vector<vector<ci>> newgraphs(vector<info>ls, int deletes) {
	vector<vector<ci>> tmp;
	tmp.assign(n + 1, vector<ci>());
	for (int i = 0; i < ls.size(); i++) {
		if (i == deletes)continue;
		int a = ls[i].a;
		int b = ls[i].b;
		int t = ls[i].t;
		tmp[a].push_back({ b,t });
		tmp[b].push_back({ a,t });
	}
	return tmp;
}


int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n >> m;
	dist.assign(n + 1, INF);
	before.assign(n + 1, -1);
	//graphs.assign(n + 1, vector<ci>());
	for (int i = 0; i < m; i++) {
		cin >> a >> b >> t;
		graphs[a][b] = t;
		graphs[b][a] = t;
		//graphs[a].push_back({ b,t });
		//graphs[b].push_back({ a,t });
		lists.push_back({ a,b,t });
	}
	//아무것도 없을때 최단거리 
	int de = dijkstra();


	//영향을 주는경우 -> 최단 경로상의 간선을 없애는 경우 
	//n을 모두 탐색할 필요 x 

	int maxs = -1;

	int N = n;


	while (N > 0) {

		dist.assign(n + 1, INF);
		int la = N;
		int lb = before[N];
		if (lb < 0)break;
		int lt = graphs[la][lb];
		graphs[la][lb] = 0;
		graphs[lb][la] = 0;

		int af = dijkstra();
		if (af == INF) { //못빠져나감 

			cout << -1;
			return 0;
		}
		int diff = af - de;
		if (maxs < diff)maxs = diff;
		graphs[la][lb] = lt;
		graphs[lb][la] = lt;
		N = lb;

	}

	cout << maxs;


}
#include <iostream>
using namespace std;
int n, m, h;
bool ladder_pos[31][11];
int ladder_cnt; // ���μ��� �߰��� ����
bool flag = false;

void dfs(int y, int cnt) {
	if (ladder_cnt == cnt) {
		bool possible = true; // ������ ���μ��� �� �����ߴ��� ����üũ
		for (int i = 1; i <= n; i++) { // ���μ�
			int verti = i;
			for (int j = 0; j < h; j++) { // ���μ�
				int hight = j;

				if (ladder_pos[hight][verti]) { // ���������� ���� ���
					verti++;
				}
				else if (verti > 1 && ladder_pos[hight][verti - 1]) {
					//�������� ���� ���
					verti--;
				}
			}
			if (verti != i) { // �߸��� ���μ�
				possible = false;
				break;
			}
		}
		if (possible) {
			flag = true; // ����
		}
		return;
	}

	// ���μ� �߰��ϴ� �ڵ�
	for (int i = y; i < h; i++) {
		for (int j = 1; j < n; j++) {
			if (!ladder_pos[i][j - 1] && !ladder_pos[i][j] && !ladder_pos[i][j + 1]) {
				//��ٸ��� �߰� �� �� �ִ� ��ġ���� Ȯ��
				ladder_pos[i][j] = true; // ��ٸ� �߰�
				dfs(i, cnt + 1); // y��ǥ�� ��ٸ� �߰� ���� ī��Ʈ
				ladder_pos[i][j] = false; // �߰��� ��ٸ� ����
			}
		}
	}
	return;
}

int main() {
	ios::sync_with_stdio(false);
	cin >> n >> m >> h;

	for (int i = 0; i < m; i++) {
		int a, b;
		cin >> a >> b;
		ladder_pos[a - 1][b] = true; //�������� �� ���μ� ǥ��
	}

	for (int i = 0; i <= 3; i++) { // ���μ� �߰� �������� Ȯ��
		ladder_cnt = i;
		dfs(0, 0);
		if (flag) { // ������ ã�� ���
			cout << ladder_cnt << endl;
			return 0;
		}
	}

	cout << -1 << endl; // ������ ã�� ���� ���
	return 0;
}

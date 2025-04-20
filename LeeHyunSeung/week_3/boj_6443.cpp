#include <cstdio>
#include <cstring>

using namespace std;

int alphabet[26] = { 0, };
int result[20];

int size = 0;
int result_index = 0;

void anagram() {
	if (result_index == size) {
		for (int i = 0; i < size; i++)
			printf("%c", result[i]);
		printf("\n");
		return;
	}

	for (int i = 0; i < 26; i++) {
		if (!alphabet[i])
			continue;

		result[result_index] = 97 + i;

		result_index++;
		alphabet[i]--;

		anagram();

		result_index--;
		alphabet[i]++;
	}
}

int main() {
	int num;
	
	scanf("%d", &num);
	for (int t = 0; t < num; t++) {
		char word[21];
		size = 0;
		result_index = 0;
		memset(alphabet, 0, sizeof(alphabet));
		
		scanf("%s", word);

		for (int i = 0; i < 20; i++) {
			if (word[i] == '\0')
				break;

			alphabet[word[i] - 97]++;
			size++;
		}

		anagram();
	}
}
#include <stdio.h>



void prt(int x[][5],int N) {




}

int main() {
	int len_y_tmp;
	scanf("%d", &len_y_tmp);
	const int len_y = len_y_tmp;

	int numbers[len_y][5];
	for (int i = 0; i < 20; i++)
	{
		int inst_x = i % 5;
		int inst_y = (int)i / 5;
		int tmp_input;
		scanf("%d", &tmp_input);
		numbers[inst_y][inst_x] = tmp_input;
	}
	//prt()


	return 0;
}
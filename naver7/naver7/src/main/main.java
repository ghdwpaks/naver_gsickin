package main;

import java.util.Scanner;

public class main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		while (true) {
			
		
			System.out.println("��� ����");
			int select_mod = sc.nextInt();
			
			if (select_mod == 1) {
				System.out.println("0�� ������ ��� ����");
				String input_string = sc.next();
				boolean pass = check_pw(input_string);
				if (pass) {
					System.out.println("�޴� ����\n1.��ǰ �߰�\n2.��� Ȯ��\n0.����� ���");
					int select_work = sc.nextInt();
					if (select_work == 1) {
						//���⿡ ��ǰ �ְ� �ڵ� �Է�
						
					} else if(select_work == 2) {
						//���⿡ ��� Ȯ�� �ڵ� �Է�
						
					} else if(select_work == 0) {
						continue;
					}
					
					
				}
			}
		}
		
	}
	public static boolean check_pw(String input_string) {
		boolean result = false;
		if (input_string == "��й�ȣ") {
			result = true;
		}
		return result;
	}
	
}

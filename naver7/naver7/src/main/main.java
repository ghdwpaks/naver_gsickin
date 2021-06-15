package main;

import java.util.Scanner;

public class main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		while (true) {
			
		
			System.out.println("모드 선택");
			int select_mod = sc.nextInt();
			
			if (select_mod == 1) {
				System.out.println("0번 관리자 모드 선택");
				String input_string = sc.next();
				boolean pass = check_pw(input_string);
				if (pass) {
					System.out.println("메뉴 선택\n1.약품 추가\n2.재고 확인\n0.사용자 모드");
					int select_work = sc.nextInt();
					if (select_work == 1) {
						//여기에 약품 주가 코드 입력
						
					} else if(select_work == 2) {
						//여기에 재고 확인 코드 입력
						
					} else if(select_work == 0) {
						continue;
					}
					
					
				}
			}
		}
		
	}
	public static boolean check_pw(String input_string) {
		boolean result = false;
		if (input_string == "비밀번호") {
			result = true;
		}
		return result;
	}
	
}

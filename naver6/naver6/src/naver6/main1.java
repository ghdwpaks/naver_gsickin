package naver6;

import java.util.*;

public class main1 {

	public static void main(String[] args) {
		
		
		Scanner sc = new Scanner(System.in);
		int count = 0;
		System.out.print("�ʺ��� ���ڸ���? ");
		String keyword = sc.next();
		while(true) {
			String carnum = sc.next();
			if (carnum.equals("0")) {
				break;
			}
			if (carnum.charAt(3) == keyword.charAt(0)) {
				count++;
			}
			
		}
		System.out.println("\n�ʺ��� ���� ���� ��� :"+count);
		
	}

}

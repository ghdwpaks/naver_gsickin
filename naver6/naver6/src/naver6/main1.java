package naver6;

import java.util.*;

public class main1 {

	public static void main(String[] args) {
		
		
		Scanner sc = new Scanner(System.in);
		int count = 0;
		System.out.print("십부제 끝자리수? ");
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
		System.out.println("\n십부제 위반 차량 대수 :"+count);
		
	}

}

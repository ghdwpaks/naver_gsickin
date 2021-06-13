package naver4;

import java.util.NoSuchElementException;

public class pro2 {

	public static void main(String[] args) {
		String s = "of the people, by the people, for the people";
		try {
			showTokens(s, ", ");
		} catch (NoSuchElementException e) {
			System.out.println("³¡");
		}

	}
	public static void showTokens(String s,String keys) {
		int j = -1;
		while (true) {
			j++;
			boolean canpass = true;
			for (int i = 0; i < keys.length(); i++) {
				if(s.charAt(j) == keys.charAt(i)) {
					System.out.println("");
					canpass = false;
					continue;
				}
			}
			if (canpass) {
				System.out.print(s.charAt(j));
			}
			if (s.length()-1 == j) {
				break;
			}
		}
	}
}

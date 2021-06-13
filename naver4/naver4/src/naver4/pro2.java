package naver4;

import java.util.NoSuchElementException;

public class pro2 {

	public static void main(String[] args) {
		String s = "of the people, by the people, for the people";
		try {
			showTokens(s, ", ");
		} catch (NoSuchElementException e) {
			// TODO: handle exception
			System.out.println("³¡");
		}

	}
	public static void showTokens(String s,String keys) {
		int j = -1;
		//System.out.println(s.length());
		while (true) {
			j++;
			//System.out.println("{ j = "+j);
			boolean canpass = true;
			for (int i = 0; i < keys.length(); i++) {
				/*
				System.out.println();
				System.out.println("s.charAt("+j+") = "+s.charAt(j));
				System.out.println("keys.charAt("+i+") = "+keys.charAt(i));
				System.out.println("s.charAt("+j+") == keys.charAt("+i+") : "+(s.charAt(j) == keys.charAt(i)));
				System.out.println();
				*/
				if(s.charAt(j) == keys.charAt(i)) {
					System.out.println("");
					canpass = false;
					continue;
				}
			}
			if (canpass) {
				System.out.print(s.charAt(j));
				//System.out.print("prints = '"+s.charAt(j)+"'");
				//System.out.println("\n}");
			}
			if (s.length()-1 == j) {
				break;
			}
			//System.out.print("j = "+j);
		}
	}
}

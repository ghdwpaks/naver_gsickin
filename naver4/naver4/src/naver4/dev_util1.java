package naver4;

public class dev_util1 {

	public static void main(String[] args) {
		System.out.print(1);
		System.out.println(2);
		String s1 = "ghdwpaks";
		String s2 = "ghdwpaks2";
		
		for (int i = 0; i < s1.length(); i++) {
			for (int j = 0; j < s2.length(); j++) {
				System.out.println("i : "+i);
				System.out.println("s1["+i+"] = "+s1.charAt(i));
				System.out.println("\t\tj : "+j);
				System.out.println("\t\ts2["+j+"] = "+s2.charAt(j));
			}
			System.out.println("\n\n\n\n");
		}

	}

}

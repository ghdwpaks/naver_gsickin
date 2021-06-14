package naver6;

public class main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String url = "http://hell.com/?pw=8936,id='fsfds'";
		
		int location = url.indexOf("pw=");
		String str2 = url.substring(location+7);
		String str1 = url.substring(0,location+3);
		System.out.println(str1+"****"+str2);
		
	}
}

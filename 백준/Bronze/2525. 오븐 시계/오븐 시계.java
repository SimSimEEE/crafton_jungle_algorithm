import java.util.*;

public class Main {
	public static void main(String[] args) {
		
		int A,B,C;
		
		Scanner sc = new Scanner(System.in);
		
		A = sc.nextInt();
		B = sc.nextInt();
		C = sc.nextInt();
		
		System.out.println((A+(B+C)/60)%24 + " " + (B + C)%60 );
		
		
	}
}
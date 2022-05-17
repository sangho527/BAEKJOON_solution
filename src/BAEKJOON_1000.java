import java.util.Scanner; // Scanner 클래스 임포트, Scanner 첫 단어는 반드시 대문자 !

public class BAEKJOON_1000 {
    public static void main(String[] args) {
        Scanner sc = new Scanner (System.in);   // 객체명 선언
        int a = sc.nextInt();   // 정수입력
        int b = sc.nextInt();   // 정수입력
        System.out.println(a+b);    // 출력
        sc.close();
    }
}


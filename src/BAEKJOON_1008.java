import java.util.Scanner; // 스캐너 선언

public class BAEKJOON_1008 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in); // 스캐너로 입력받음
        double a = sc.nextDouble(); // double 정수형으로 받아서 출력값 소수점 아래 9자리이상 표현
        double b = sc.nextDouble();
        sc.close();
        System.out.print(a/b); //출력
    }
}

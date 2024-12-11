import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // N, M 입력받기
        int N = sc.nextInt();
        int M = sc.nextInt();

        // 배열 입력받기
        int[] arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }

        int result = 0;

        // 삼중 루프를 사용하여 세 숫자의 합 계산
        for (int i = 0; i < N; i++) {
            for (int j = i + 1; j < N; j++) {
                for (int k = j + 1; k < N; k++) {
                    int arrSum = arr[i] + arr[j] + arr[k];

                    // M 이하의 합 중 가장 큰 값 찾기
                    if (arrSum <= M && arrSum > result) {
                        result = arrSum;
                    }
                }
            }
        }
        System.out.println(result);
    }
}
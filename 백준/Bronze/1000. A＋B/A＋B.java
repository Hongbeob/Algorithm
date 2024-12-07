import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();
        String[] numbers = input.split(" ");
        int A = Integer.parseInt(numbers[0]);
        int B = Integer.parseInt(numbers[1]);
        System.out.println(A+B);
    }
}

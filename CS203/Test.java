package CS203;
import java.util.Scanner;

public class Test {
    public static void main(String[] args) {
        Scanner scnr = new Scanner(System.in);
        NewTestClass test = new NewTestClass(scnr);
        System.out.println(test.toString());
    }
}

package CS203.Lab8;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Driver {
    public static void main(String[] args)throws FileNotFoundException {
        Scanner scnr = new Scanner(System.in);
        StudentTester tester = new StudentTester();
        System.out.println("Input File path and name to read.");
        tester.setList(scnr.nextLine());
        System.out.println("Input file destination.");
        tester.printList(scnr.nextLine());
        scnr.close();
    }
}

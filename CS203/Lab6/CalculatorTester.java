package CS203.Lab6;

import java.util.Scanner;

public class CalculatorTester {
    public static void main(String[] args) {
        Scanner scnr = new Scanner(System.in);
        System.out.println("Input two integers.");
        ScientificCalculator cal = new ScientificCalculator(scnr.nextInt(), scnr.nextInt());
        scnr.close();

        System.out.println(cal.add());
        System.out.println(cal.subtract());
        System.out.println(cal.divide());
        System.out.println(cal.multiply());
        System.out.println(cal.exponent());
        System.out.println(cal.squareRoot());

    }
}

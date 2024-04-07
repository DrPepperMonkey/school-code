package Lab10;

import java.util.Scanner;

public class Calculator {
    public static void main(String[] args) {
        GUI gui = new GUI();
    }

    public double add(double input1, double input2) {
        return input1 + input2;
    }

    public double subtract(double input1, double input2) {
        return input1 - input2;
    }

    public double multiply(double input1, double input2) {
        return input1 * input2;
    }

    public double divide (double input1, double input2) {
        return input1 / input2;
    }
}
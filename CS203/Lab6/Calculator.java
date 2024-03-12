package CS203.Lab6;

public class Calculator {
    private int num1;
    private int num2;

    public Calculator(int numb1, int numb2) {
        num1 = numb1;
        num2 = numb2;
    }

    public void setNum1(int num) {
        num1 = num;
    }

    public int getNum1() {
        return num1;
    }

    public void setNum2(int num) {
        num2 = num;
    }

    public int getNum2() {
        return num2;
    }

    public int add() {
        return (num1 + num2);
    }

    public int subtract() {
        return (num1 - num2);
    }

    public int multiply() {
        return (num1 * num2);
    }

    public double divide() {
        double dint1 = num1;
        double dint2 = num2;
        return (dint1 / dint2);
    }
}

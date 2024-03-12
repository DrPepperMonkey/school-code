package CS203.Lab6;

public class ScientificCalculator extends Calculator {

    public ScientificCalculator(int numb1, int numb2) {
        super(numb1, numb2);
    }
    public double squareRoot() {
        return Math.pow(this.getNum1(), 0.5);
    }

    public double exponent() {
        return Math.pow(this.getNum1(), this.getNum2());
    }
}

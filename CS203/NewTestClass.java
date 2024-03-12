package CS203;
import java.util.Scanner;

public class NewTestClass extends TestClass{
    private String var4;

    public NewTestClass(Scanner scnr) {
        super(scnr);
        var4 = scnr.next();
    }

    public String getVar4() {
        return this.var4;
    }

    public String toString() {
        return (this.getVar1() + this.getVar2() + this.getVar3() + this.getVar4());
    }
}

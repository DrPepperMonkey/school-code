package CS203;
import java.util.Scanner;



public class TestClass {
    private String var1;
    private String var2;
    private String var3;
    TestClass(Scanner scnr) {
        this.var1 = scnr.next();
        this.var2 = scnr.next();
        this.var3 = scnr.next();
    }

    public String getVar1() {
        return this.var1;
    }

    public String getVar2() {
        return this.var2;
    }

    public String getVar3() {
        return this.var3;
    }

    public String toString() {
        return (this.getVar1() + this.getVar2() + this.getVar3());
    }
}

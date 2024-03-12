package CS203.HW3;
import java.util.Scanner;

public class UABPerson {
    private String firstName;
    private String lastName;
    private String blazerID;
    private String var;
    
    public UABPerson(String input) {
        Scanner scnr = new Scanner(input);
        this.firstName = scnr.next();
        this.lastName = scnr.next();
        this.blazerID = scnr.next();
        scnr.close();
    }

    public void setFirstName(String firstNameIn) {
        this.firstName = firstNameIn;
    }

    public String getFirstName() {
        return this.firstName;
    }

    public void setLastName(String lastNameIn) {
        this.lastName = lastNameIn;
    }

    public String getLastName() {
        return this.lastName;
    }

    public void setBlazerID(String BIDIn) {
        this.blazerID = BIDIn;
    }

    public void setVar(String input) {
        this.var = input;
    }

    public String getVar() {
        return this.var;
    }

    public String getBlazerID() {
        return this.blazerID;
    }

}

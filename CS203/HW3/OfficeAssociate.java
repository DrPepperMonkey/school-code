package CS203.HW3;
import java.util.Scanner;

public class OfficeAssociate extends UABPerson{
    private String role;
    private String department;

    public OfficeAssociate(String input) {
            super(input);
            super.setVar("Office Associates:");
            Scanner scnr = new Scanner(input);
            for (int i = 0; i < 3; i++) {
                scnr.next();
            }
            this.role = scnr.next();
            this.department = scnr.next();
            scnr.close();
    }

    public void setDepartment(String departmentIn) {
        this.department = departmentIn;
    }

    public String getDepartment() {
        return this.department;
    }

    public void setRole(String roleIn) {
        this.role = roleIn;
    }

    public String getRole() {
        return this.role;
    }

    public String getVar() {
        return "Office Associates";
    }

    public String toString() {
        return ("Name: " + this.getFirstName() + " " + this.getLastName() 
            + " BlazerId: " + this.getBlazerID() 
            + " Role: " + this.getRole() 
            + " Department: " + this.getDepartment());
    }

}

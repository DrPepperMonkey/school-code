package CS203.HW3;
import java.util.Scanner;

public class MedicalStaff extends UABPerson{
    private String role;
    private String department;

    public MedicalStaff(String input) {
            super(input);
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

}

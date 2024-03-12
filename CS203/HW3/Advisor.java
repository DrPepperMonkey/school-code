package CS203.HW3;
import java.util.Scanner;

public class Advisor extends UABPerson{
    private String department;
    private String group;

    public Advisor(String input) {
            super(input);
            super.setVar("Advisors:");
            Scanner scnr = new Scanner(input);
            for (int i = 0; i < 3; i++) {
                scnr.next();
            }
            this.department = scnr.next();
            this.group = scnr.next();
            scnr.close();
        }

        public void setDepartment(String departmentIn) {
            this.department = departmentIn;
        }

        public String getDepartment() {
            return this.department;
        }

        public void setGroup(String groupIn) {
            this.group = groupIn;
        }

        public String getGroup() {
            return this.group;
        }

        public String toString(){
            return ("Name: " + this.getFirstName() + " " + this.getLastName() 
            + " BlazerId: " + this.getBlazerID() 
            + " Department: " + this.getDepartment()
            + " Group: " + this.getGroup());
        }
}

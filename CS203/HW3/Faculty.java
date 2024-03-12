package CS203.HW3;
import java.util.Scanner;

public class Faculty extends UABPerson{
    private String department;
    private String courses;

    public Faculty(String input) {
            super(input);
            super.setVar("Faculty:");
            Scanner scnr = new Scanner(input);
            for (int i = 0; i < 3; i++) {
                scnr.next();
            }
            this.department = scnr.next();
            this.courses = scnr.next();
            scnr.close();
        }

    public void setDepartment(String departmentIn) {
        this.department = departmentIn;
    }

    public String getDepartment() {
        return this.department;
    }

    public void setCourses(String coursesIn) {
        this.courses = coursesIn;
    }

    public String getCourses() {
        return this.courses;
    }

    public String getVar() {
        return "Faculty";
    }
    
    public String toString() {
        return ("Name: " + this.getFirstName() + " " + this.getLastName() 
            + " BlazerId: " + this.getBlazerID() 
            + " Department: " + this.getDepartment()
            + " Courses: " + this.getCourses());
    }
}

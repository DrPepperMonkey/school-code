package CS203.HW3;
import java.util.Scanner;

public class Student extends UABPerson{
    private String GPA;
    private String level;
    private String major;

    public Student(String input) {
        super(input);
        super.setVar("Students:");
        Scanner scnr = new Scanner(input);
        for (int i = 0; i < 3; i++) {
            scnr.next();
        }
        this.level = scnr.next();
        this.major = scnr.next();
        this.GPA = scnr.next();
        scnr.close();
    }

    public void setGPA(String GPAIn) {
        this.GPA = GPAIn;
    }

    public String getGPA() {
        return this.GPA;
    }

    public void setLevel(String levelIn) {
        this.level = levelIn;
    }

    public String getLevel() {
        return this.level;
    }

    public void setMajor(String majorIn) {
        this.major = majorIn;
    }

    public String getMajor() {
        return this.major;
    }

    public String toString() {
        return ("Name: " + this.getFirstName() + " " + this.getLastName() 
        + " BlazerId: " + this.getBlazerID() 
        + " Level: " + this.getLevel() 
        + " Major: " + this.getMajor() 
        + " GPA: " + this.getGPA());
    }
}

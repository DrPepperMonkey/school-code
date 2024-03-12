package CS203.HW3;
import java.util.Scanner;

public class Nurse extends MedicalStaff{
    private String onCall;

    public Nurse (String input) {
            super(input);
            super.setVar("Nurses:");
            Scanner scnr = new Scanner(input);
            for (int i = 0; i < 5; i++) {
                scnr.next();
            }
            this.onCall = scnr.next();
            scnr.close();
        }

    public void setOnCall(String onCallIn) {
        this.onCall = onCallIn;
    }

    public String getOnCall() {
        return this.onCall;
    }

    public String getVar() {
        return "Nurses";
    }

    public String toString() {
        return ("Name: " + this.getFirstName() + " " + this.getLastName() 
            + " BlazerId: " + this.getBlazerID() + " Role: " + this.getRole() 
            + " Department: " + this.getDepartment() + " " + getOnCall());
    }
}

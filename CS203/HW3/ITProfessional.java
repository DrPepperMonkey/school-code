package CS203.HW3;
import java.util.Scanner;

public class ITProfessional extends UABPerson{
    private String team;
    
    public ITProfessional(String input) {
        super(input);
        super.setVar("IT Professionals:");
        Scanner scnr = new Scanner(input);
        for (int i = 0; i < 3; i++) {
            scnr.next();
        }
        this.team = scnr.next();
        scnr.close();
    }

    public void setTeam(String teamIn) {
        this.team = teamIn;
    }

    public String getTeam() {
        return this.team;
    }

    public String getVar() {
        return "IT Professionals";
    }

    public String toString() {
        return ("Name: " + this.getFirstName() + " " + this.getLastName() 
            + " BlazerId: " + this.getBlazerID() 
            + " Team: " + this.getTeam());
    }
}

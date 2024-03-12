package CS203.HW3;

public class Doctor extends MedicalStaff{
    public Doctor(String input) {
            super(input);
            super.setVar("Doctors:");
    }

    public String getVar() {
        return "Doctors";
    }

    public String toString() {
        return ("Name: " + this.getFirstName() + " " + this.getLastName() 
            + " BlazerId: " + this.getBlazerID() + " Role: " + this.getRole() 
            + " Department: " + this.getDepartment());
    }
    
}

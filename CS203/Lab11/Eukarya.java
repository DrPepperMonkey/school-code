package CS203.Lab11;

public class Eukarya extends Organism{

    public Eukarya() {
        super();
        super.changeKey("domain", "Eukarya");
        super.addAttribute("hasDoubleMembraneNucleus", true);
        super.addAttribute("hasMembraneBoundOrganelles", true);
        super.addAttribute("doesMitosis", true);
        
    }

    public void summary() {
        System.out.println("Domain Eukarya has the following classification: "
            + super.getClassification());
        System.out.println("Eukarya has the following attributes: " 
            + super.getAttributes());
        System.out.println("");
    }

    public void addAttribute(String key, Boolean value) {
        super.addAttribute(key, value);
    }


}

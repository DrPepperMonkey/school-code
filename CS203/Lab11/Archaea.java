package CS203.Lab11;

public class Archaea extends Organism{
    
    public Archaea() {
        super();
        super.changeKey("domain", "Archaea");
        super.addAttribute("hasCircularChromosomes", true);
    }

    public void summary() {
        System.out.println("Domain Archaea has the following classification: "
            + super.getClassification());
        System.out.println("Domain Archaea has the following attributes: "
            + super.getAttributes());
        System.out.println("");
    }

    public void addAttribute(String key, Boolean value) {
        super.addAttribute(key, value);
    }
}

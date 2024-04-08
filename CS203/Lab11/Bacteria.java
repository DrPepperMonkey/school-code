package CS203.Lab11;

public class Bacteria extends Organism{

    public Bacteria() {
        super();
        super.changeKey("domain", "Bacteria");
        super.addAttribute("hasNucleus", true);
    }

    public void summary() {
        System.out.println("Domain Bacteria has the following classification: "
            + super.getClassification());
        System.out.println("Domain Bacteria has the following attributes: "
            + super.getAttributes());
        System.out.println("");
    }

    public void addAttribute(String key, Boolean value) {
        super.addAttribute(key, value);
    }
}

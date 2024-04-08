package CS203.Lab11;

public class Animalia extends Eukarya {
    
    public Animalia() {
        super();
        super.changeKey("kingdom", "animalia");
        super.addAttribute("hasGameets", true);
    }

    public void summary() {
        System.out.println("Kingdom Animalia has the following classification: "
            + super.getClassification());
        System.out.println("Kingdom Animalia has the following attributes: " 
            + super.getAttributes());
        System.out.println("");
    }

    public void eat(String food) {
        System.out.println(super.getClassification().get("genus")
            + " " + super.getClassification().get("species") + " ate " + food);
    }
}

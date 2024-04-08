package CS203.Lab11;

public class Driver {
    public static void main(String[] args) {
        Animalia animalia = new Animalia();
        Organism archaea = new Archaea();
        Organism bacteria = new Bacteria();
        Organism eukarya = new Eukarya();
        Organism[] organisms = {animalia, archaea, bacteria, eukarya};
        for (Organism i: organisms) {
            i.addAttribute("isAlive", true);
            i.summary();
        }
        animalia.changeKey("genus", "Oryctolagus");
        animalia.changeKey("species", "cuniculus");
        animalia.eat("turnips");
    }
}

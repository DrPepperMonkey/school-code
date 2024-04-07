package CS203.Lab11;
import java.util.HashMap;

public abstract class Organism {
    private HashMap<String, String> classification;

    public Organism(String[] nameIn){
        String[] categories = {"domain", "kingdom", "phylum", "class", 
            "order", "family", "genus", "species"};
        for (int i = 0; i < 8; i++) {
            this.classification.put(categories[i], nameIn[i]);
        }
    }

    public abstract String toString();

    public void changeKey(String catIn, String newVal) {
        if (this.classification.containsKey(catIn)) {
            this.classification.put(catIn, newVal);
        }
        else {
            System.out.println("Please choose from the following");
        }
    }
}

package CS203.Lab11;
import java.util.HashMap;

public abstract class Organism {
    private HashMap<String, String> classification;
    private HashMap<String, Boolean> attributes;

    public Organism(){
        classification = new HashMap<>();
        attributes = new HashMap<>();
        String[] categories = {"domain", "kingdom", "phylum", "class", 
            "order", "family", "genus", "species"};
        for (int i = 0; i < 8; i++) {
            this.classification.put(categories[i], null);
        }
    }

    public abstract void summary();

    public void changeKey(String catIn, String newVal) {
        if (this.classification.containsKey(catIn)) {
            this.classification.put(catIn, newVal);
        }
    }

    public void addAttribute(String key, Boolean value) {
        attributes.put(key, value);
    }

    public HashMap<String, Boolean> getAttributes() {
        return this.attributes;
    }

    public HashMap<String, String> getClassification() {
        return this.classification;
    }
}

package CS203.HW4;

import java.util.HashMap;

public class Espresso extends Coffee{

    private HashMap<String, Boolean> addOns = new HashMap<>();
    private int shots;
    
    public Espresso(double priceIn) {
        super(priceIn);
        this.shots = 1;
        this.addOns.put("whipped", false);
        this.addOns.put("chocolate", false);
    }

    public void setAddOns(String key, boolean value) {
        this.addOns.put(key, value);
    }

    public HashMap<String, Boolean> getAddOns() {
        return this.addOns;
    }

    public void setShots(int shotsIn) {
        this.shots = shotsIn;
    }

    public int getShots() {
        return this.shots;
    }

    public void prepare() {
        System.out.println("Add " + Integer.toString(shots) + " shots of espresso.");
        switch (this.getBrew()) {
            case 1:     //Americano
                System.out.println("Add " + Integer.toString(2 * this.getShots()) + " shots of water.");
                break;
            case 2:     //Latte
                System.out.println("Add " + Double.toString(2 * this.getShots() / 3) + " Shots of steamed milk.");
                System.out.println("Add thin layer of foam.");
                break;
            default:    //Mocha
                System.out.println("Add 1tsp of chocolate chips");
                System.out.println("Add " + Integer.toString(2 * this.getShots()) + " shots of water.");
                break;
        }
        if (this.getAddOns().get("whipped").equals(true)) {
            System.out.println("Add whipped cream.");
        }
        if (this.getAddOns().get("chocolate").equals(true)) {
            System.out.println("Add chocolate syrup.");
        }
    }
}

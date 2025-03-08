package CS203.HW4;

public class RegularCustomer extends Customer{
    

    public RegularCustomer(String nameIn) {
        super(nameIn);
    }

    public void payCoffee() {
        System.out.println("Regular customer can pay for the " + 
            "coffee using credit card or cash.");
    }
}

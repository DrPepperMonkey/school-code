package CS203.HW4;

public class PremiumCustomer extends Customer{
    

    public PremiumCustomer(String nameIn) {
        super(nameIn);
    }

    public void payCoffee() {
        System.out.println("Premium customer can pay for the coffee using " + 
        "bitcoin, credit card, or cash. A 10% discount will be applied to the price.");
    }
}

package CS203.HW4;

public abstract class Customer {
    private String name;


    public Customer(String nameIn) {
        this.name = nameIn;
    }

    public void setName(String nameIn) {
        this.name = nameIn;
    }

    public String getName() {
        return this.name;
    }

    public abstract void payCoffee();
}

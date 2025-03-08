package CS203.HW4;

public abstract class Coffee {

    private double price;
    private int brew;
    private boolean status;

    public Coffee(double priceIn) {
        this.price = priceIn;
        this.status = true;
    }

    public void setPrice(double priceIn) {
        this.price = priceIn;
    }

    public double getPrice() {
        return this.price;
    }

    public void setBrew(int brewIn) {
        this.brew = brewIn;
    }

    public int getBrew() {
        return this.brew;
    }

    public void setStatus(boolean statusIn) {
        this.status = statusIn;
        //true = active
        //false = passive
    }

    public boolean getStatus() {
        return this.status;
    }

    public abstract void prepare();

}

package CS203.HW4;


public abstract class FilteredCoffee extends Coffee {

    

    public FilteredCoffee(double priceIn) {
        super(priceIn);
    }


    public void prepare() {
        System.out.println("Scoop one ounce of coffee grounds.");
        System.out.println("Add 6 ounces of water.");
        switch (this.getBrew()) {
            case 1 :    //light roast
                System.out.println("Brew for 5 minutes.");
                break;
            case 2:     //medium roast
                System.out.println("Brew for 7 minutes.");
                break;

            default:    //dark roast
                System.out.println("Brew for 9 minutes.");
                break;
        }
        setStatus(false);
    }
}

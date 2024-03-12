package CS203.HW3;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.io.PrintWriter;

public class CLI {
    private ReadIn read = new ReadIn();
    private ArrayList<String> file = new ArrayList<>();
    private int choice;
    private String fileName;
    
    public CLI(String input) throws FileNotFoundException {
        this.fileName = input;
        read.setUABPeople(read.setFileString(this.fileName));
        read.reading();
        this.file = read.getUABPeople();
    }

    public void driver(int i, String perChar, String perString) throws FileNotFoundException{

        switch(i) {
            case(0):
                this.file.add((perChar + " " + perString));
                this.write(this.file);
                break;

            case(1):
                this.file.remove(this.choice);
                this.write(this.file);
                break;

            case(2):
                ArrayList<ArrayList<UABPerson>> listUABP = read.getListUABP();
                System.out.println("Welcome to the UAB Employee System");
                System.out.println("");
                System.out.println("The UAB System has the following employees:");
                System.out.println("");
                System.out.println("Total number of employees: " + read.getUABPeople().size());
                for (int k = 0; k < listUABP.size(); k++) {
                    System.out.println("");
                    ArrayList<UABPerson> tmp = listUABP.get(k);
                    for (int j = 0; j < tmp.size(); j++) {
                        if (j == 0) {
                            System.out.println(tmp.get(0).getVar());
                        }
                        System.out.println(tmp.get(j).toString());
                    }
                }
                break;
        }
    }

    public void setChoice(int input) {
        this.choice = input;
    }

    public void write(ArrayList<String> input) throws FileNotFoundException {
        PrintWriter writer = new PrintWriter(this.fileName);
        for (int i = 0; i < input.size(); i ++) {
            writer.println(input.get(i));
        }
        writer.close();
    }

    public ArrayList<String> getFile() {
        return this.file;
    }

    public String displayFile() {
        String output = "";
        for (int j = 0; j < this.file.size(); j++) {
            output += ("[" + Integer.toString(j) + "] " + this.file.get(j) + "\n");
        }
        return output;
    }

}

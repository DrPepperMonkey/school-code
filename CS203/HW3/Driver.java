package CS203.HW3;
import java.util.Scanner;
import java.io.FileNotFoundException;

public class Driver {
    
    public static void main(String[] args)throws FileNotFoundException {
        Scanner scnr = new Scanner(System.in);
        System.out.println("Add[0], Remove[1], View[2] a UABPerson, or Exit[3].");
        int input = scnr.nextInt();
        scnr.nextLine();
        String perChar = "";
        String perString = "";
        if (input == 0 || input == 1 || input == 2) {
            System.out.println("Input file path to read.");
            CLI cli = new CLI(scnr.nextLine());
            if (input == 0) {
                System.out.println("Please choose a type of UABPerson.");
                System.out.println("Advisor[A], Faculty[F], ITProfessionial[I] " + 
                    "Medical Staff[M], Office Associate[O], Student[S].");
                perChar = scnr.next();
                scnr.nextLine();
                System.out.println("Input UABPerson to add.");
                String tmp = scnr.nextLine();
                perString = tmp;
            }
            else if (input == 1) {
                System.out.println(cli.displayFile());
                System.out.println("Choose from list ");
                cli.setChoice(scnr.nextInt());
            }
            else {
                perChar = null;
                perString = null;
            }
            cli.driver(input, perChar, perString);
            main(args);
        }
        scnr.close();
    }

}

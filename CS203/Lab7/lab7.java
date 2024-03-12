package CS203.Lab7;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.io.PrintWriter;

public class lab7 {
    public static void main(String[] args) throws FileNotFoundException{
        File file = new File("tester.txt");
        Scanner scnr = new Scanner(file);
        PrintWriter writer = new PrintWriter("output.txt");
        while (scnr.hasNextLine()) {
            Scanner line = new Scanner(scnr.nextLine());
            line.useDelimiter(",");
            int newInt = 0;
            while (line.hasNextInt()) {
                newInt += line.nextInt();
            }
            writer.println(newInt);
            line.close();
        }
        scnr.close();
        writer.close();
    }
}

package CS203.Lab8;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.ArrayList;
import java.io.PrintWriter;

public class StudentTester {
    private ArrayList<Student> list = new ArrayList<>();

    void setList(String fileIn)throws FileNotFoundException {
        File file = new File(fileIn);
        Scanner scnr = new Scanner(file);
        while (scnr.hasNextLine()) {
            Scanner line = new Scanner(scnr.nextLine());
            Student stu = new Student();
            line.useDelimiter(",");
            stu.setName(line.next());
            stu.setExam1(line.nextInt());
            stu.setExam2(line.nextInt());
            stu.setExam3(line.nextInt());
            stu.setFinalGrade();
            stu.setLetterGrade();
            list.add(stu);
            line.close();
        }
        scnr.close();
    }

    void printList(String fileOut)throws FileNotFoundException {
        PrintWriter writer = new PrintWriter(fileOut);
        for (int i = 0; i < list.size(); i++) {
            writer.println(list.get(i).toString());
        }
        writer.close();
    }
}

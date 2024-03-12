package CS203.Lab8;

public class Student {
    private String name;
    private int exam1;
    private int exam2;
    private int exam3;
    private double finalGrade;
    private String letterGrade;

    void student(
        String nameIn, int exam1In, int exam2In, int exam3In,
        double finalGradeIn, String letterGradeIn) {
        this.name = nameIn;
        this.exam1 = exam1In;
        this.exam2 = exam2In;
        this.exam3 = exam3In;
        this.finalGrade = finalGradeIn;
        this.letterGrade = letterGradeIn;

    }

    void setName(String nameIn) {
        this.name = nameIn;
    }

    String getName() {
        return this.name;
    }

    void setExam1(int gradeIn) {
        this.exam1 = gradeIn;
    }

    int getExam1() {
        return this.exam1;
    }

    void setExam2(int gradeIn) {
        this.exam2 = gradeIn;
    }

    int getExam2() {
        return this.exam2;
    }

    void setExam3(int gradeIn) {
        this.exam3 = gradeIn;
    }

    int getExam3() {
        return this.exam3;
    }

    void setFinalGrade() {
        this.finalGrade = 
            (0.25 * this.exam1) + 
            (0.25 * this.exam2) + 
            (0.5 * exam3);
    } 

    double getFinalGrade() {
        return this.finalGrade;
    }

    void setLetterGrade() {
        double grade = this.getFinalGrade();
        
        if (grade >= 90) {
            this.letterGrade = "A";
        }
        else if (grade >= 80 && grade < 90) {
            this.letterGrade = "B";
        }
        else if (grade >= 70 && grade < 80) {
            this.letterGrade = "C";
        }
        else {
            this.letterGrade = "F";
        }
    }

    String getLetterGrade() {
        return this.letterGrade;
    }

    public String toString() {
        return (this.getName() + " received a grade of " + 
            this.getFinalGrade() + ": " + this.getLetterGrade());
    }
}

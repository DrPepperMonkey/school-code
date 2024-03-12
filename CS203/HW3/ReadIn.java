package CS203.HW3;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class ReadIn {
    private ArrayList<String> UABPeople = new ArrayList<>();
    private ArrayList<ArrayList<UABPerson>> listUABP = new ArrayList<>();
    private ArrayList<UABPerson> students = new ArrayList<>();
    private ArrayList<UABPerson> faculty = new ArrayList<>();
    private ArrayList<UABPerson> ITPeople = new ArrayList<>();
    private ArrayList<UABPerson> medicalStaff = new ArrayList<>();
    private ArrayList<UABPerson> advisors = new ArrayList<>();
    private ArrayList<UABPerson> officeAssociates = new ArrayList<>();
    private ArrayList<UABPerson> doctors = new ArrayList<>();
    private ArrayList<UABPerson> nurses = new ArrayList<>();

    public ArrayList<String> setFileString (String input)throws FileNotFoundException {
        ArrayList<String> fileList = new ArrayList<>();
        File file = new File(input);
        Scanner fScanner = new Scanner(file);
        while (fScanner.hasNextLine()) {
            fileList.add(fScanner.nextLine());
        }
        fScanner.close();
        return fileList;
    }
    
    public void reading() throws FileNotFoundException{
        ArrayList<String> file = this.getUABPeople();
        for (int i = 0; i < file.size(); i++){
            Scanner scnr  = new Scanner(file.get(i));
            String sw = scnr.next();
            String person = "";
            while (scnr.hasNext()) {
                person += (scnr.next() + " ");
            }
            switch (sw) {
                case ("S"):
                    UABPerson stu = new Student(person);
                    this.students.add(stu);
                    break;

                case ("F"):
                    UABPerson fac = new Faculty(person);
                    this.faculty.add(fac);
                    break;

                case ("I"):
                    UABPerson ITP = new ITProfessional(person);
                    this.ITPeople.add(ITP);
                    break;

                case("O"):
                    UABPerson off = new OfficeAssociate(person);
                    this.officeAssociates.add(off);
                    break;

                case ("A"):
                    UABPerson adv = new Advisor(person);
                    this.advisors.add(adv);
                    break;

                case ("M"):
                    MedicalStaff medi = new MedicalStaff(person);
                    this.medicalStaff.add(medi);
                    if (medi.getRole().equals("Nurse")) {
                        MedicalStaff nurse = new Nurse(person);
                        this.nurses.add(nurse);
                    }
                    else {
                        MedicalStaff doc = new Doctor(person);
                        this.doctors.add(doc);
                    }
                    break;
            }
            scnr.close();
        }
        setListUABP();
    }

    public void setUABPeople(ArrayList<String> input) {
        this.UABPeople = input;
    }

    public void setListUABP() {
        this.listUABP.add(this.ITPeople);
        this.listUABP.add(this.students);
        this.listUABP.add(this.advisors);
        this.listUABP.add(this.faculty);
        this.listUABP.add(this.nurses);
        this.listUABP.add(this.doctors);
        this.listUABP.add(this.officeAssociates);
    }

    public ArrayList<ArrayList<UABPerson>> getListUABP() {
        return this.listUABP;
    }

    public ArrayList<String> getUABPeople() {
        return this.UABPeople;
    }

    public ArrayList<UABPerson> getStudents(){
        return this.students;
    }

    public ArrayList<UABPerson> getAdvisors() {
        return this.advisors;
    }

    public ArrayList<UABPerson> getFaculty() {
        return this.faculty;
    }

    public ArrayList<UABPerson> getITPeople() {
        return this.ITPeople;
    }

    public ArrayList<UABPerson> getMedicalStaff() {
        return this.medicalStaff;
    }

    public ArrayList<UABPerson> getOfficeAssociates() {
        return this.officeAssociates;
    }

    public ArrayList<UABPerson> getNurses() {
        return this.nurses;
    }

    public ArrayList<UABPerson> getDoctors() {
        return this.doctors;
    }
}

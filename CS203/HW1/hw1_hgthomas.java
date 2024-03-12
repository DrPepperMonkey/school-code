package CS203.HW1;


public class hw1_hgthomas {
    public static void main(String[] args) {
        //Task 1: calculateBMI
        double bmi1 = calculateBMI(70, 1.75);
        double bmi2 = calculateBMI(85, 1.80);
        System.out.println("BMI 1: " + bmi1);
        System.out.println("BMI 2: " + bmi2);
        //Task 2: blazerNumber
        boolean blazerNumber1 = blazerNumber(28);
        boolean blazerNumber2 = blazerNumber(12);
        System.out.println("Blazer Number 1: " + blazerNumber1);
        System.out.println("Blazer Number 2: " + blazerNumber2);
        //Task 3: findLargestPrime
        int largestPrime1 = findLargestPrime(20);
        int largestPrime2 = findLargestPrime(50);
        System.out.println("Largest Prime 1: " + largestPrime1);
        System.out.println("Largest Prime 2: " + largestPrime2);
        //Task 4: numSteps
        int numSteps1 = numSteps(14);
        int numSteps2 = numSteps(5);
        System.out.println("Number of Steps 1: " + numSteps1);
        System.out.println("Number of Steps 2: " + numSteps2);
        //Task 5: countVowelConsonants
        countVowelConsonants("hello");
        countVowelConsonants("programming");
    }

    public static double calculateBMI(double weight, double height) {
        return(weight / Math.pow(height, 2));
    }

    public static boolean blazerNumber(int n2) {
        int sum = 0;
        for (int i=1; i<n2; i++) {
            if (n2%i == 0){
                sum += i;
            }
        }
        if (n2 != sum) {
            return(true);
        }

        else {
            return(false);
        }
    }

    public static int findLargestPrime(int maxNum) {
        boolean tmp = true;
        for (int i=2; i<maxNum; i++){
            if ((maxNum % i) == 0) {
                tmp = false;
            }
        }
        if (tmp == true) {
            return(maxNum);
        }

        else {
            return(findLargestPrime(maxNum-1));
        }
    }

    public static int numSteps(int n) {
        int steps = 0;
        int i = n;
        while (i != 0)
            if ((i%2) != 0) {
                i--;
                steps++;
            }
            else {
                i /= 2;
                steps++;
            }
        return(steps);
    }

    public static void countVowelConsonants(String s) {
        int vcount = 0;
        int ccount = 0;
        String vowels = "aeiou";
        for (int i=0; i<s.length(); i++) {
            if (vowels.contains(s.toLowerCase().substring(i, (i+1)))) {
                vcount++;
            }
            else {
                ccount++;
            }
        }
        System.out.println("Number of Vowels and Consonants in " + 
            "\"" + s + "\": " + vcount + ", " + ccount);
    }
    
}

import java.util.Scanner;

public class stdgradecalcodsoftA70 {

   
    public static char calculateGrade(double average) {
        if (average >= 90) {
            return 'A';
        } else if (average >= 80) {
            return 'B';
        } else if (average >= 70) {
            return 'C';
        } else if (average >= 60) {
            return 'D';
        } else {
            return 'F';
        }
    }

   
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Welcome to Student Grade Calculator!");

        
        System.out.print("Enter the number of subjects: ");
        int numSubjects = sc.nextInt();

        
        double[] scores = new double[numSubjects];
        double total = 0;

        
        for (int i = 0; i < numSubjects; i++) {
            System.out.print("Enter the score for subject " + (i + 1) + ": ");
            scores[i] = sc.nextDouble();
            total += scores[i];
        }

        
        double average = total / numSubjects;

        
        char grade = calculateGrade(average);

        
        System.out.println("Total Score: " + total);
        System.out.println("Average Score: " + average);
        System.out.println("Final Grade: " + grade);

        sc.close();
    }
}

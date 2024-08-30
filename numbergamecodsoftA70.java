import java.util.Scanner;

public class numbergamecodsoftA70 {
    public static void guessingNumberGame() {
        Scanner sc = new Scanner(System.in);
        int rounds = 0;
        int totalScore = 0;

        while (true) {
            // Increment round counter
            rounds++;
            int number = 1 + (int) (100 * Math.random());

            int K = 5;
            int i, guess;
            int score = 0;

            System.out.println("Round " + rounds + ": A number is chosen between 1 to 100. Guess the number within " + K + " trials.");

            for (i = 0; i < K; i++) {
                System.out.println("Attempt " + (i + 1) + ": Guess the number:");
                guess = sc.nextInt();

                if (number == guess) {
                    System.out.println("Congratulations! You guessed the number.");
                    score = K - i; // Score is based on remaining attempts
                    totalScore += score;
                    break;
                } else if (number > guess && i != K - 1) {
                    System.out.println("The number is greater than " + guess);
                } else if (number < guess && i != K - 1) {
                    System.out.println("The number is less than " + guess);
                }
            }

            if (i == K) {
                System.out.println("You have exhausted " + K + " trials.");
                System.out.println("The number was " + number);
            }

            System.out.println("Your score in this round: " + score);
            System.out.println("Total score: " + totalScore);

            System.out.println("Do you want to play again? (yes/no)");
            String playAgain = sc.next();

            if (!playAgain.equalsIgnoreCase("yes")) {
                break;
            }
        }

        System.out.println("Game over! Your final score after " + rounds + " rounds is: " + totalScore);
    }

    public static void main(String arg[]) {
        // Function Call
        guessingNumberGame();
    }
}

import java.util.Scanner;

public class cccodsoftA70 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Sample exchange rates (replace with actual rates)
        double usdToEur = 0.9;
        double usdToGbp = 0.75;
        double usdToInr = 82;
        double eurToUsd = 1.11;
        double eurToGbp = 0.83;
        double eurToInr = 91;
        double gbpToUsd = 1.33;
        double gbpToEur = 1.2;
        double gbpToInr = 110;
        double inrToUsd = 0.012;
        double inrToEur = 0.011;
        double inrToGbp = 0.009;

        System.out.println("Currency Converter");
        System.out.println("Available currencies: USD, EUR, GBP, INR");

        while (true) {
            System.out.print("Enter the amount: ");
            double amount = scanner.nextDouble();

            System.out.print("Enter the source currency (USD, EUR, GBP, INR): ");
            String sourceCurrency = scanner.next().toUpperCase();

            System.out.print("Enter the target currency (USD, EUR, GBP, INR): ");
            String targetCurrency = scanner.next().toUpperCase();

            double convertedAmount = 0;

            // Conversion logic (replace with a more efficient method)
            if (sourceCurrency.equals("USD")) {
                if (targetCurrency.equals("EUR")) {
                    convertedAmount = amount * usdToEur;
                } else if (targetCurrency.equals("GBP")) {
                    convertedAmount = amount * usdToGbp;
                } else if (targetCurrency.equals("INR")) {
                    convertedAmount = amount * usdToInr;
                } else {
                    System.out.println("Invalid target currency.");
                    continue;
                }
            } else if (sourceCurrency.equals("EUR")) {
                // ... similar logic for EUR conversions
            } else if (sourceCurrency.equals("GBP")) {
                // ... similar logic for GBP conversions
            } else if (sourceCurrency.equals("INR")) {
                // ... similar logic for INR conversions
            } else {
                System.out.println("Invalid source currency.");
                continue;
            }

            System.out.println(amount + " " + sourceCurrency + " is equal to " + convertedAmount + " " + targetCurrency);

            System.out.println("Do you want to convert another amount? (yes/no)");
            String answer = scanner.next();
            if (!answer.equalsIgnoreCase("yes")) {
                break;
            }
        }

        scanner.close();
    }
}
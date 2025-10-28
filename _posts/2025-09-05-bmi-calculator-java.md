---
layout: post
title: "BMI Calculator in Java"
date: 2025-09-05 10:00:00 +0400
categories: [Java, CS Foundations]
tags: [Java, BMI, Console Programs, Beginner]
permalink: /post/
---

This Java console program prompts the user to enter their weight (in pounds) and height (in inches), then calculates their Body Mass Index (BMI) and displays the category.

The output is formatted to one decimal place to match standard BMI ranges.

---

## Features

- Uses `Scanner` for input
- Converts imperial units to metric
- Applies BMI formula: `weight (kg) / height² (m²)`
- Displays result with formatted decimal output
- Aligns BMI ranges for readability

---

## Code Implementation

```java
// Import Scanner to handle user input
import java.util.Scanner;
 
// Main class for assignment logic
public class Assignment2_BMI_Calculator {

    // The main method runs the program
    public static void main(String[] args) {    
        // Define and initialize variables for values to be input
        double bmi;                // bmi value to be calculated
        double weightPounds;       // weight in pounds value to be input
        double heightInches;       // height in inches value to be input
        double weightKg;           // weight in kilograms to be calculated
        double heightMeters;       // height in meters to be calculated

        try (Scanner input = new Scanner( System.in )) {
            // Add two blank lines in the output
            System.out.println( "\n\n" );

            // Prompt the user for weight in pounds
            System.out.print("Enter your weight in pounds: ");
            weightPounds = input.nextDouble(); // Input weight value

            // Prompt the user for height in inches
            System.out.print("Enter your height in inches: ");
            heightInches = input.nextDouble(); // Input height value
            
            // Convert pounds to kilograms and inches to meters
            weightKg = weightPounds * 0.45359237;
            heightMeters = heightInches * 0.0254;

            // Calculate BMI
            bmi = weightKg / (heightMeters * heightMeters);

            // Display the result with one decimal place
        System.out.printf("\nYour BMI is: %.1f\n", bmi);

        // Display BMI title
        System.out.println("\nBody Mass Index");

        // Display row separator
        System.out.println( "---------------" );

        // Display categories and ranges column headings
        System.out.println("Categories      Ranges");

        // Display row separator
        System.out.println("----------      ------");
        
        // Display BMI categories and ranges for user evaluation
        System.out.printf("%-15s %s\n", "Underweight:", "less than 18.5");
        System.out.printf("%-15s %s\n", "Normal:", "18.5 - 24.9");
        System.out.printf("%-15s %s\n", "Overweight:", "25 - 29.9");
        System.out.printf("%-15s %s\n", "Obese:", "30 or greater");

        // Add two blank lines in the output
        System.out.println( "\n\n" );
          // Catch input errors like non-numeric values
        } catch (Exception e) {
            System.err.println("Error reading input: " + e.getMessage());
        }
    }
}
```

## Sample Output
![Console output showing Body Mass Index (BMI)](/assets/img/bmi-calculator.png)  

## Notes
- System.out.printf is used here to cleanly control decimal output
- Variables were declared clearly and spaced logically for readability
- Considered consistent indentation and header comments

## Related Posts
- [C++: LeetCode Easy – Two Sum](https://anthony-reese.github.io/posts/2025-03-02-leetcode-167-two-sum-ii-input-array-is-sorted.markdown)
- [Java: Print "JAVA" Pattern](https://anthony-reese.github.io/posts/2025-08-28-java-pattern.md)
---
layout: post
title: "BMI Calculator in Java"
date: 2025-09-05 10:00:00 +0400
categories: [Java, CS Foundations]
tags: [Java, BMI, Console Programs, Beginner]
permalink: /posts/2025-09-05-bmi-calculator-java
---

## Overview
This Java console program prompts the user to enter their weight (in pounds) and height (in inches), then calculates their Body Mass Index (BMI) and displays the category.

The output is formatted to one decimal place to match standard BMI ranges.

## Features

- Uses `Scanner` for input
- Converts imperial units to metric
- Applies BMI formula: `weight (kg) / height² (m²)`
- Displays result with formatted decimal output
- Aligns BMI ranges for readability

## Code Implementation

```java

import java.util.Scanner;
 
public class BMI_Calculator {
    public static void main(String[] args) {    
        double bmi;
        double weightPounds;
        double heightInches;
        double weightKg;
        double heightMeters;

        try (Scanner input = new Scanner( System.in )) {
            System.out.println( "\n\n" );
            System.out.print("Enter your weight in pounds: ");
            weightPounds = input.nextDouble();
            System.out.print("Enter your height in inches: ");
            heightInches = input.nextDouble();
            weightKg = weightPounds * 0.45359237;
            heightMeters = heightInches * 0.0254;

            bmi = weightKg / (heightMeters * heightMeters);

        System.out.printf("\nYour BMI is: %.1f\n", bmi);
        System.out.println("\nBody Mass Index");
        System.out.println( "---------------" );
        System.out.println("Categories      Ranges");
        System.out.println("----------      ------");
        System.out.printf("%-15s %s\n", "Underweight:", "less than 18.5");
        System.out.printf("%-15s %s\n", "Normal:", "18.5 - 24.9");
        System.out.printf("%-15s %s\n", "Overweight:", "25 - 29.9");
        System.out.printf("%-15s %s\n", "Obese:", "30 or greater");
        System.out.println( "\n\n" );
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
- [C++: LeetCode Easy – Two Sum]({{ site.baseurl }}/posts/2025-03-02-leetcode-167-two-sum-ii-input-array-is-sorted)
- [Java: Print "JAVA" Pattern]({{ site.baseurl }}/posts/2025-08-28-java-pattern)
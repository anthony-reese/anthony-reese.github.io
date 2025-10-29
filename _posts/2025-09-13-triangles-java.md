---
layout: post
title: "Triangles in Java"
date: 2025-09-13 10:00:00 +0400
categories: [Java, CS Foundations]
tags: [Java, Console Programs, Beginner]
permalink: /posts/2025-09-13-triangles
---

## Overview
This Java console program lets the user choose how many rows of asterisks to print and select between two patterns: an increasing triangle (“Pine Tree”) or a decreasing triangle (“Tornado”).
The program demonstrates nested loops and a switch statement, key control structures for iterative pattern generation.

## Features

- User-defined number of rows (size of the pattern)  
- Two selectable patterns:  
  - Pine Tree – increasing asterisk rows  
  - Tornado – decreasing asterisk rows  
- Implements nested for loops for pattern generation  
- Uses a switch statement for user choice handling  
- Displays clean console output with spacing for readability  
- Simple and beginner-friendly structure  

## Code Implementation

```java
import java.util.Scanner;

public class Triangles {
    public static void main(String[] args) {
        try (Scanner input = new Scanner( System.in )) {
            int numAsterisks;
            int choice;
            System.out.println();
            System.out.print("Enter the maximum number of rows of asterisks to print: ");
            numAsterisks = input.nextInt();
            System.out.println();
            System.out.println("Choose a pattern:");
            System.out.println("1. Pine Tree");
            System.out.println("2. Tornado");
            System.out.println();
            System.out.print("Enter your choice: ");
            choice = input.nextInt();
            System.out.println();

            switch (choice) {
                case 1 -> {
                    for (int i = 1; i <= numAsterisks; i++) {
                        for (int j = 1; j <= i; j++) {
                            System.out.print("*");
                        }
                        System.out.println();
                    }
                }

                case 2 -> {
                    for (int i = numAsterisks; i >= 1; i--) {
                        for (int j = 1; j <= i; j++) {
                            System.out.print("*");
                        }
                        System.out.println();
                    }
                }
                default -> System.out.println("Invalid pattern choice. Please choose 1 or 2.");
            }
            System.out.println();
        } catch (Exception e) {
            System.err.println("Error reading input: " + e.getMessage());
        }
    }
}
```

## Sample Output
![Console output showing Triangles](/assets/img/triangles.png)

## Notes

- Designed for console execution in Java (no GUI); assumes valid integer input from the user
- Ideal for beginners learning loops and conditional branching
- Demonstrates incremental and decremental iteration logic
- Compatible with Java 17+

## Related Posts

[Guess The Number]({{ site.baseurl }}/posts/2025-09-13-guess-the-number)
---
layout: post
title: "Guess the Number in Java"
date: 2025-09-13 10:00:00 +0400
categories: [Java, CS Foundations]
tags: [Java, Console Programs, Beginner]
permalink: /posts/2025-09-13-guess-the-number
---

## Overview
This program prompts the user to guess a secret number within a user-defined range and limited number of attempts.  
It provides hints (“too high” or “too low”) and allows replay after each round.

## Features
- User-defined range (`1` to `N`)
- User-defined maximum guesses
- Random number generation using `Math.random()`
- Feedback on each attempt
- Option to replay multiple rounds
- Graceful termination message
- Safe input handling via `try-with-resources`

## Code Implementation

```java
import java.util.Scanner;

public class GuessTheNumber {
    public static void main(String[] args) {
        try (Scanner input = new Scanner( System.in )) {
            boolean playAgain = true;

            while (playAgain) {
                System.out.println();
                System.out.print("Enter the maximum number for the secret number: ");
                int N = input.nextInt();
                System.out.println();
                System.out.print("Enter the maximum number of guesses allowed: ");
                int maxGuesses = input.nextInt();
                System.out.println();
                int secretNumber = (int) (N * Math.random()) + 1;
                int guessCount = 0;
                boolean guessedCorrectly = false;

                while (guessCount < maxGuesses && !guessedCorrectly) {
                    System.out.print("Enter your guess: ");
                    int guess = input.nextInt();
                    guessCount++;
                    System.out.println();

                    if (guess == secretNumber) {
                        System.out.println("Correct! You guessed the number in " + guessCount + " tries.");
                        guessedCorrectly = true;
                        System.out.println();

                    } else if (guess < secretNumber) {
                        System.out.println("Too low!");
                        System.out.println();

                    } else {
                        System.out.println("Too high!");
                        System.out.println();
                    }
                }
                if (!guessedCorrectly) {
                    System.out.println("Sorry, you did not guess the number. The secret was " + secretNumber + ".");
                }

                System.out.println();
                System.out.print("Do you want to play again? (yes/no): ");
                String response = input.next();
                System.out.println();

                if (!response.equalsIgnoreCase("yes")) {
                    playAgain = false;
                    System.out.println("Thanks for playing!");
                    System.out.println();
                }
            }
        } catch (Exception e) {
            System.err.println("Error reading input: " + e.getMessage());
        }
    }
}
```

## Sample Output
![Console output from the Guess the Number Java program](/assets/img/guess-the-number.png)

## Notes

- Designed for console execution in Java (no GUI)
- Assumes valid numeric input (exception handling out of scope)
- Ideal for beginners learning loops and branching
- Compatible with Java 17+  

## Related Posts

[Triangles]({{ site.baseurl }}/posts/2025-09-13-triangles)
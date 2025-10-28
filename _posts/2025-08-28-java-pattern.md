---
layout: post
title: "Print 'JAVA' Pattern in Java"
date: 2025-08-28 11:00:00 +0400
categories: [Java, CS Foundations]
tags: [Java, Patterns, Console Output, Beginner]
permalink: /post/
---

A simple Java program that prints a stylized "JAVA" pattern using `System.out.println`.

## Code Implementation

```java
public class JavaPattern {
    public static void main(String[] args) {
        // Print an empty line to separate output from the top of the screen
        System.out.println();
        // Print each line with a letter of "JAVA" in a pattern
        System.out.println("    J    A    V       V    A");
        System.out.println("    J   A A    V     V    A A");
        System.out.println("J   J  AAAAA    V   V    AAAAA");
        System.out.println(" J J  A     A     V     A     A");
        // Print an empty line to separate output from the bottom of the screen
        System.out.println();
    }
}
```

## Sample Output
![Console output showing the word JAVA printed in a stylized format](/assets/img/java-pattern.png) 

## Technical Contributions and Reflection
- Structure of a Java class and `main()` method
- Console output with proper alignment
- Indentation style and spacing for clean output

## Process Insights
- Manual alignment using spaces
- The importance of structure and formatting in code
- Writing clean, readable, and well-commented code from the beginning

## Related Posts
- [BMI Calculator in Java](https://anthony-reese.github.io/posts/2025-09-05-bmi-calculator-java.md)

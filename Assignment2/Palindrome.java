/*
 * Write the Palindrome program inside the main method
 * according to the assignment description.
 * 
 * To compile:
 *        javac Palindrome.java
 * To execute:
 *        java Palindrome 5 4 6 6 4 5
 * 
 * DO NOT change the class name
 * DO NOT use System.exit()
 * DO NOT change add import statements
 * DO NOT add project statement
 * 
 */

public class Palindrome {
    public static void main(String[] args) {
       
        // WRITE YOUR CODE HERE
        int N1 = Integer.parseInt(args[0]);
        int N2 = Integer.parseInt(args[1]);
        int N3 = Integer.parseInt(args[2]);
        int N4 = Integer.parseInt(args[3]);
        int N5 = Integer.parseInt(args[4]);
        int N6 = Integer.parseInt(args[5]);
        System.out.println(N1 == N6 && N2 == N5 && N3 == N4);

    }
}

/*
 * Write your program inside the main method to compute the 
 * Gravitational Force according to the assignment description.
 * 
 * To compile:
 *        javac GravitationalForce.java
 * To execute:
 *        java GravitationalForce 36000.0 1080.0 50.0
 * 
 * DO NOT change the class name
 * DO NOT use System.exit()
 * DO NOT change add import statements
 * DO NOT add project statement
 * 
 */

public class GravitationalForce {

    public static void main(String[] args) {
       
        // WRITE YOUR CODE HERE
        double g = 6.6743*Math.pow(10,-11);
        double m1 = Double.parseDouble(args[0]);
        double m2 = Double.parseDouble(args[1]);
        double r = Double.parseDouble(args[2]);
        if (r<=0) {
            System.out.println("Error, r is not positive");
        }
        else {
            double force = g*(m1*m2) / (r*r);
            System.out.println(force);
        }
    }
}


package edu.nuaa.testing;

public class App {
    public static int sum(int a, int b) { return a + b; }

    public static double divide(double a, double b) {
        if (b == 0) throw new IllegalArgumentException("b must not be zero");
        return a / b;
    }

    public static void main(String[] args) {
        System.out.println("Hello NUAA Advanced Testing!");
    }
}

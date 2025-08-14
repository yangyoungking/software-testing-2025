
package edu.nuaa.testing;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class AppTest {
    @Test
    void testSum() {
        assertEquals(7, App.sum(3, 4));
        assertEquals(0, App.sum(-5, 5));
    }

    @Test
    void testDivide() {
        assertEquals(2.5, App.divide(5.0, 2.0), 1e-9);
    }

    @Test
    void testDivideByZero() {
        assertThrows(IllegalArgumentException.class, () -> App.divide(1.0, 0.0));
    }
}

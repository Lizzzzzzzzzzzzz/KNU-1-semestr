package testing02;

import org.junit.Test;
import org.junit.jupiter.api.BeforeAll;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertThrows;

public class TestProgram {
    public void TestProgram() {

    }
    private static FizzBuzz FizzBuzz;
    @BeforeAll
    static void createObject() {
        FizzBuzz = new Program();

    }

    @Test
     public void testInput() {
        FizzBuzz.print(0);
    }
    @Test
    public void testInputIncorrectInput() {
        assertThrows(
                IllegalArgumentException.class,
                ()-> FizzBuzz.print(-3));
        assertThrows(
                IllegalArgumentException.class,
                ()-> FizzBuzz.print(123));;

    }
    @Test
    public void testFizz() {
        assertEquals("Fizz", FizzBuzz.print(3));
        assertEquals("Fizz", FizzBuzz.print(6));
        assertEquals("Fizz", FizzBuzz.print(9));
        assertEquals("Fizz", FizzBuzz.print(12));
        assertEquals("Fizz", FizzBuzz.print(15));
    }
    @Test
    public void testBuzz() {
        assertEquals("Buzz", FizzBuzz.print(5));
        assertEquals("Buzz", FizzBuzz.print(10));
        assertEquals("Buzz", FizzBuzz.print(15));
        assertEquals("Buzz", FizzBuzz.print(20));
        }
    @Test
    public void testFizzBuzz() {
        assertEquals("FizzBuzz", FizzBuzz.print(15));
        assertEquals("FizzBuzz", FizzBuzz.print(45));
    }
    @Test
    public void testNumber() {
        assertEquals("1", FizzBuzz.print(15));
        assertEquals("2", FizzBuzz.print(2));

    }


}



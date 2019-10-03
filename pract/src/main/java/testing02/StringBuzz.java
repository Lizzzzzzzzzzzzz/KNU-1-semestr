package testing02;

import org.junit.Test;
import org.junit.jupiter.api.BeforeAll;

public interface StringBuzz {
    void populate(String[] args);

    class TestBuzzClassTest {
        private static StringBuzz TestBuzzClass;

        @BeforeAll
        void createObject() {
        FizzBuzzClass = new StringBuzz();
        }


        @Test
        void TestIncorrectInput() {
        FizzBuzzClass
        }


    }
}

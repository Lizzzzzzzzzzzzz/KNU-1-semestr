package testing02;

import org.junit.Test;

public class TestProgram {
    public void TestProgram() {}
    @Test
     public void testInput() {
        new Program().print(0);
    }
    @Test
    public void testInputIncorrectLess() {
        new Program().print(-1);
        }

    @Test
    public void testInputIncorrentGreatest() {
        new Program().print(123);
    }
}



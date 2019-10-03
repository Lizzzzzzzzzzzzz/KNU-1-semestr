package testing02;

public class Program implements FizzBuzz {

    @Override
    public String print(int number) {
        if (number<0) {
            throw new IllegalArgumentException("число меньше 1");
        }
        if (number>100) {
            throw new IllegalArgumentException("число больше 100");
        }
        return "";

    }
}

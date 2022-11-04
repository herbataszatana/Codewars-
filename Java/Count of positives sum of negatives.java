public class Kata
{
    public static int[] countPositivesSumNegatives(int[] input)
    {
       if (input == null || input.length == 0) return new int[] {};
       int positive = 0;
       int negative = 0;
       for (int i : input) {
         if (i > 0) positive ++;
         if (i < 0) negative += i;
       }
       return new int[] {positive,negative};
    }
}
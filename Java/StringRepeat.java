public class Solution {
    public static String repeatStr(final int repeat, final String string) {
      StringBuilder str = new StringBuilder ();     
      for (int i = 0; i < repeat; i++) {
        str.append(string); 
      }
      String singleString = str.toString();
      System.out.println(singleString);
      return singleString;
    }
}
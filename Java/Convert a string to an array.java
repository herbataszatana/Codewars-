public class Solution {

    public static String[] stringToArray(String s) {
      String[] array = s.split(" ");
      if(array.length > 0){
        for(String i: array){
            System.out.print(i +" ");}}
      return array;
    }
}
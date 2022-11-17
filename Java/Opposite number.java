public class Kata
    {
        public static int opposite(int number)
        {
         int answer = 0;
            // your code here
          if (number > 0){
            answer = 0 - number;
             System.out.println(number);
            System.out.println(answer);
          }
          else {
            answer = answer - number;
             System.out.println(number);
             System.out.println(answer);
          }
          return answer; 
        }
    }
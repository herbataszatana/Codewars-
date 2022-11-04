class Kata {
  public static String getMiddle(String word) {
    //Code goes here!
    int len = word.length();
    String middle = ""; 
    int reminder =  len % 2;
    int half = len/2;
    //Check if odd or even 
    if (reminder == 0){
      // Even
      middle = word.substring(half - 1, half + 1);
    } 
    
    else{
      middle = word.substring(half, half + 1);
     }
  return middle;   
  }
}
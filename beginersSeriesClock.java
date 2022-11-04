public class Clock
{
  public static int Past(int h, int m, int s) 
  {
    //Happy Coding! ^_^
    int hour = h * 3600000;
    int minute = m * 60000;
    int second = s * 1000; 
    int past = hour + minute + second; 
  return past;
  }
}
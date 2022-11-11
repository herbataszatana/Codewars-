public class Alarm {
  
  public static boolean setAlarm(boolean employed, boolean vacation) {
    // Your code here...
    boolean alarm = false;
    if (employed & vacation ){
      alarm = false;
    }
    else if (!employed & vacation ){
       alarm = false;
    }
    else if (!employed & !vacation ){
       alarm = false;
    }
    else {
       alarm = true;
    }
    return alarm;
  }
}
public class Calculate {
  public static String bmi(double weight, double height) {
    //bmi calculation 
    String response = ""; 
    double bmi = weight/(height*height); 
    
    System.out.println(bmi);
    if (bmi<= 18.5){
      response = "Underweight";
    }
    else if (bmi <= 25.0){
      response = "Normal";
    }
    else if (bmi <= 30){
      response = "Overweight";
    }
    else if (bmi > 30){
     response = "Obese";
    }
    return response;
  }
}
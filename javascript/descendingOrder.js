function descendingOrder(n){
    str = n.toString();
    arr = str.split("");
    sorted = arr.sort();
    descSort = sorted.reverse();
    // convert to num and return 
        // join to one string
        descStr = descSort.join("");
        // convert to number
        number = parseInt(descStr);
    //retun the number 
    console.log(number);
    return number;
  }

  descendingOrder(809);
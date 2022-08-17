function toAcronym(inp){
    arr = [];
    string = "";
    arr = inp.split(" ");
    for (i=0; i< arr.length; i++){
        word = arr[i].split('').reverse().join('');
        acronym = word.substr(word.length-1);
        string = string + acronym; 
    }
    console.log(string.toUpperCase());
    return string.toUpperCase();
    console.log(string.toUpperCase());

}


toAcronym('My acronym machine is amazing');
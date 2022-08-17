function solution(str, ending){
    // TODO: complete
    strArr = str.split('').reverse().join(''); //reversed string
    stringend = strArr.substr(0, ending.length); // last two letters 
    stringend = stringend.split('').reverse().join('');
    return (stringend === ending);
  }

solution('abcde', 'cde');
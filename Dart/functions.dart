num addTwo(num1, num2){
  return num1 + num2;
}
num subtractTwo(num1, num2){
  return num1 - num2;
}
num multiplyTwo(num1, num2){
  return num1 * num2;
}

num divideTwo(num1, num2) => num1 / num2;

int stringLength(String word){
  return word.length;

}

getFirstElement(List){
  return List[0];
}
void main(){
  print(getFirstElement(["Ian", "Mikkel", "Sheila"]));
}
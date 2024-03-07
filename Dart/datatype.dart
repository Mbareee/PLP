void main(){
  String motherName = "Jane";
  int age = 54;
  double bankBalance = 10000000.22;
  List<String> children = ["Ian", "Sheila", "Mikkel"];


Map childrenAges = {
  "Ian": 27,
  "Sheila": 22,
  "Mikkel": 6,
};
print('''My mother's name is $motherName. She is currently $age years old. 
After years of hardwork she currently has $bankBalance ksh in her account which 
she will share with her children ${children[0]}, ${children[1]} and ${children[2]}.
The oldest child is ${childrenAges["Ian"]} years old and will most likely get the
largest share''');
}
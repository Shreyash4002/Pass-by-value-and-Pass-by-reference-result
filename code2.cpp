#include <iostream>
int n;
int expo(int x){
return x= x*x;
}
int& exporef(int &x){//return by reference
x = x*x;
return x;
}
int main() {
std::cout<<"Enter a Number:\n";
scanf("%d", &n);
std::cout<<"Call by value and return by value result :"<<expo(n)<<std::endl;
std::cout<<"Call by Reference and return by reference result:"<<exporef(n);
}
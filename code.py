#include <iostream>
#include <string.h>
using namespace std;
//pass by value-result
void swap(int &a, int &b)
{
int temp;
temp = a;
a = b;
b = temp;
}
int main()
{
int value = 2;
int list[] = {1, 3, 5};
int temp1 = value;
int temp2 = list[0];
swap(temp1, temp2);
value = temp1;
list[0] = temp2;
cout << value << " " << list[0] << endl;
value = temp1;
list[0] = temp2;
temp2 = list[1];
swap(temp1, temp2);
cout << value << " " << list[1] << endl;
value = temp1;
list[1] = temp2;
temp2 = list[2];
swap(temp1, temp2);
cout << value << " " << list[2] << endl;
value = temp1;
list[2] = temp2;
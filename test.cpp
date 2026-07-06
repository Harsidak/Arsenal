#include <iostream>


int main(){
    int a = 9, b = 10;
    int temp = a;
    a = b;
    b = temp;
    std::cout << a << " " << b;
    return 0;
}
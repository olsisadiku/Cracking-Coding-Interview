#include <list>
#include <string>
#include<iostream>

using namespace std;

template <typename T>
void delete_middle(list<T>& l){
    
}

int main(){

    list<int> l = { 7, 5, 16, 8, 7, 5 };

    delete_middle();
    list<int>::iterator it;

    for(it = l.begin(); it != l.end(); ++it){
        cout << *it << endl;  
    }


    return 0;
}
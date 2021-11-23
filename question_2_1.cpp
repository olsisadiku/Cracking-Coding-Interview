#include <list>
#include <iostream>
#include <map>

using namespace std;

template <typename T>
void remove_dups(list<T> check){
    map<T,int> checker;

    
}


int main(){
    list<int> l = { 7, 5, 16, 8, 7, 5 };

    remove_dups(l);
    list<int>::iterator it;

    for(it = l.begin(); it != l.end(); ++it){
        cout << *it << endl;  
    }

    return 0; 
}
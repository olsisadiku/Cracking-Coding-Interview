#include <list>
#include <string>
#include<iostream>

using namespace std;

template <typename T, typename F>
void delete_middle(list<T>& l, typename F::iterator elem ){
    l.erase(elem);

}

int main(){

    list<int> l = { 7, 5, 16, 8, 7, 5 };
    list<int>::iterator it1;
    it1 = l.begin();
    it1++;
    it1++;
    it1++;
    delete_middle<int, list<int>>(l, it1);
    list<int>::iterator it;

    for(it = l.begin(); it != l.end(); ++it){
        cout << *it << endl;  
    }


    return 0;
}
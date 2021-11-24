#include <list>
#include <iostream>
#include <map>

using namespace std;

template <typename T>
void remove_dups(list<T>& check){
    map<T,int> checker;

    typename list<T>::iterator it;
    it = check.begin();

    while(it != check.end()){
        T a = *it; 
        if(checker.count(a)){
            it = check.erase(it);
        }
        else{
            cout << "ran insert" << endl; 
            cout << "Inserting " << a << endl; 
            checker.insert(pair<T,int>(a, 1));
            cout << "finished insert" << endl; 
            ++it;
        }
    }
    
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
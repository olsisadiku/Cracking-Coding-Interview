#include <list>
#include <iostream>

using namespace std;

template <typename T>
T find_k(list<T>& l, int k){
    int index = k - 1;

    typename list<T>::iterator it;
    it = l.begin();
    int counter = 0; 
    while(it != l.end()){
        if(counter == l.size() - k){
            return *it;
        }
        else{
            counter++;
            ++it;
        }
    }

}

int main(){
    list<char> l = {'a','b','c','d'  };

    cout << find_k(l, 3) << endl;

    return 0; 
}
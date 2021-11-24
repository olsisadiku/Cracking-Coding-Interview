#include <list>
#include <string>
#include<iostream>

using namespace std;

template <typename T>
bool is_palindrome(list<T>& l){
    typename list<T>::iterator beg = l.begin();
    typename list<T>::iterator end = l.end();
    end--;
    while(beg != end){
        cout << "BEG " << *beg << " END " << *end << endl;
        if(*beg == *end)
        {
            beg++;
            end--;
            continue;
        }
        else{
            return false;
        }
        
    }
    return true;
}

int main(){

    list<int> l = { 1,2,3,3,2,1 };

    cout << is_palindrome(l) << endl;
    

    return 0;
}
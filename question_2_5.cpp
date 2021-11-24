#include <list>
#include <string>
#include<iostream>
#include <math.h>

using namespace std;

list<int> backward_order(list<int>& l1, list<int> l2){
    int multiplier = 1; 
    int sum1 = 0; 
    list<int>::iterator it1; 
    it1 = l1.begin();
    while(it1 != l1.end()){
        sum1 += multiplier * (*it1);
        multiplier *= 10; 
        ++it1;
    }
    multiplier = 1;
    int sum2 = 0; 
    list<int>::iterator it2; 
    it2 = l2.begin();
    while(it2 != l2.end()){
        sum2 += multiplier * (*it2);
        multiplier *= 10; 
        ++it2;
    }

    list<int> final_l; 

    int final = sum1 + sum2; 
    while(final != 0){
        int val = final % 10;
        final /= 10; 
        final_l.push_back(val);
    }

    return final_l;

    
    
}

list<int> forward_order(list<int>& l1, list<int> l2){
    int multiplier = pow(10,l1.size() - 1);

    int sum1 = 0; 
    list<int>::iterator it1; 
    it1 = l1.begin();
    while(it1 != l1.end()){
        sum1 += multiplier * (*it1);
        multiplier /= 10; 
        ++it1;
    }

    multiplier = pow(10,l2.size() - 1);
    int sum2 = 0; 
    list<int>::iterator it2; 
    it2 = l2.begin();
    while(it2 != l2.end()){
        sum2 += multiplier * (*it2);
        multiplier /= 10; 
        ++it2;
    }

    list<int> final_l; 

    int final = sum1 + sum2; 
    while(final != 0){
        int val = final % 10;
        final /= 10; 
        final_l.push_front(val);
    }

    return final_l;
}

int main(){

    list<int> l1 = { 7,1,6 };
    list<int> l2 = { 5,9,2 };
    
    list<int> l;
    l = backward_order(l1,l2);
    list<int>::iterator it;

    for(it = l.begin(); it != l.end(); ++it){
        cout << *it << endl;  
    }


    return 0;
}
// Copyright 2017 ChenRui ruirui@bu.edu
#include <vector>
#include <string>
using namespace std;

typedef string BigInt;
typedef vector<double> Poly;

BigInt multiply_int(const BigInt &a,const BigInt &b){
	Poly d(a.size()+b.size()-1,0);
	BigInt res;
	double temp=0;
	for(int i=0;i<a.size();i++){
		for(int j=0;j<b.size();j++){
			d[i+j] += (a[i]-48) * (b[j]-48);
		}
	}
	for(int i=0;i<d.size();i++)
    res.append(to_string((int)d[i]));
	return res;
}

// Copyright 2017 ChenRui ruirui@bu.edu
#include <vector>
#include <string>
using namespace std;

typedef string BigInt;
typedef vector<int> Poly;

BigInt multiply_int(const BigInt &a,const BigInt &b){

	Poly d(a.size()+b.size()-1,0);
	BigInt res;
	for(int i=0;i<a.size();i++){
		for(int j=0;j<b.size();j++){
			d[d.size()-1-i-j] += (a[i]-48) * (b[j]-48);
		}
	}
	for(int i=0;i<(int)(d.size()-1);i++){  //d.size()-2=negative number! interesting
		d[i+1]+=d[i]/10;
		d[i]=d[i]%10;
	}
	while(d[d.size()-1]==0&& d.size()>1){
		d.pop_back();
	}
	for(int i=d.size()-1;i>=0;i--){
        res.append(to_string(d[i]));}
	return res;
}

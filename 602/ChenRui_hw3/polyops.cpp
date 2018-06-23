// Copyright 2017 ChenRui ruirui@bu.edu
#include <vector>


using namespace std;
typedef vector<double> Poly;

Poly add_poly(const Poly &a,const Poly &b){
	Poly c;
//	Poly c(1,0);
	for(int i=0;i<(a.size()>b.size()?b.size():a.size());i++){
//	if(a[i]+b[i]!=0){
		c.push_back(a[i]+b[i]);//}
	//	c[i]=a[i]+b[i]; //need initialization
	}
	if(a.size()>b.size()){		
		c.insert(c.end(),a.begin()+b.size(),a.end());
	}else{		
		c.insert(c.end(),b.begin()+a.size(),b.end());
	}
	while(c[c.size()-1]==0&& c.size()>1){

		c.pop_back();
	}
	return c;

}

Poly multiply_poly(const Poly &a,const Poly &b){
	Poly d(a.size()+b.size()-1,0);
//	Poly d(1,0);
	for(int i=0;i<a.size();i++){
		for(int j=0;j<b.size();j++){
			d[i+j] += a[i] * b[j];
		}
	}
	while(d[d.size()-1]==0&& d.size()>1){

		d.pop_back();
	}

	return d;
}

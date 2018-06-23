// copyright ChunxiWang, tracycxw@bu.edu
#include<iostream>

using namespace std;
int main(int argumentcount,char**arguments){
	/*cout<<"following is stdout:"<<endl;*/
	for(int i=1;i<=argumentcount;i++){
		if(i<5){
			cout<<arguments[i]<<endl;
		}
		else{
			/*cout<<"stderr: "<<arguments[i]<<endl;*/
			cerr<<arguments[i]<<endl;
		}
	}
	return 0;
}
#include <iostream>
using namespace std;
int main(int argumentcount,char**arguments){
	for(int i=1;i<=argumentcount;i++){
		if(i<5){
			cout<<arguments[i]<<endl;

		}else{
			cerr<<arguments[i]<<endl;
		}

	}
return 0;
}
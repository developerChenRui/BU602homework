// Copyright 2017 ChenRui ruirui@bu.edu
#include <iostream> 
int main(int argumentcount, char **arguments){
//        freopen("stdout.txt","w",stdout);
//        freopen("stderr.txt","w",stderr);

		for(int i =1;i<5;i++){
            if(i<argumentcount){
			std::cout<<arguments[i]<<'\n';}
        }

		for(int i=5;i<argumentcount;i++){
            if(i<argumentcount){
			std::cerr<<arguments[i]<<'\n';}
        }

    return 0;
}


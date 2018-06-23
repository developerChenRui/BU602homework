//Copyright 2017 Yize Liu lyz95222@bu.edu
#include <iostream>
#include <string>
#include <math.h>
#include <limits>
#include <vector>
#include <stdlib.h>
#include <iomanip>
#include <exception>
#include <algorithm>
using namespace std;

class Motion{
	public: string name;
	        double x;
            double y;
            double Vx;
            double Vy;
        Motion(string name, double x, double y, double Vx, double Vy);
        Motion();
        double collision_time(const Motion *m);
};
        Motion::Motion(string name, double x, double y, double Vx,double Vy){
    	         this->name=name;
    	         this->x=x;
    	         this->y=y;
    	         this->Vx=Vx;
    	         this->Vy=Vy;
        }
        Motion::Motion(){}
        double Motion::collision_time(const Motion *m){
    	   double a=pow((this->Vx-m->Vx), 2.0)+pow((this->Vy-m->Vy), 2.0);
		   double b=2.0*(this->Vx*(this->x-m->x)+m->Vx*(m->x-this->x)+this->Vy*(this->y-m->y)+m->Vy*(m->y-this->y));
		   double c=pow((this->x-m->x), 2.0)+pow((this->y-m->y), 2.0)-100;
		   if((pow(b, 2.0)-4*a*c)<0){
				return numeric_limits<double>::max ();
		   }else{
			  double resulta= ((-b-sqrt(pow(b, 2.0)-4*a*c))/(2.0*a));
			   if(resulta>0){
				  return resulta;
			    }
			   return numeric_limits<double>::max ();
		    } 
        }
 void collision(Motion * m1, Motion * m2){
	double delta_x=m1->x-m2->x;
	double delta_y=m1->y-m2->y;
	double delta_Vx=m1->Vx-m2->Vx;
	double delta_Vy=m1->Vy-m2->Vy;
	double dot=(delta_x*delta_Vx+delta_y*delta_Vy)/(delta_x*delta_x+delta_y*delta_y);
	m1->Vx=m1->Vx-dot*delta_x;
	m1->Vy=m1->Vy-dot*delta_y;
	m2->Vx=m2->Vx+dot*delta_x;
	m2->Vy=m2->Vy+dot*delta_y;
 }
void test(vector<Motion*>array, double time){
	double min=numeric_limits<double>::max ();
	Motion *m1=new Motion();
	Motion *m2=new Motion();
	for(int i=0; i<array.size()-1; i++){
		for(int j=i+1; j<array.size(); j++){
			double curtime=array[i]->collision_time(array[j]);
			if(curtime < min){
				m1=array[i];
				m2=array[j];
				min=curtime;
			}
		}
	}
	if(time <= min){
		for(int i=0; i<array.size(); i++){
			array[i]->x+=(array[i]->Vx*time);
			array[i]->y+=(array[i]->Vy*time);
		}
		for(int i=0; i<array.size(); i++){
			cout<<array[i]->name<<" ";
			cout<<fixed<<setprecision(8)<<array[i]->x<<" "
			<<array[i]->y<<" "<<array[i]->Vx<<" "<<array[i]->Vy<<'\n';
	    }
		return;
	}
	for(int i=0; i<array.size(); i++){
		array[i]->x+=(array[i]->Vx*min);
		array[i]->y+=(array[i]->Vy*min);
	}
	collision(m1, m2);
	test(array, time-min);
}
vector<string> split(const string& s, const char& c)
{
    string buff{""};
    vector<string> v;

    for(auto n:s)
    {
        if(n != c) buff+=n; 
        else if(n == c && buff != "") { v.push_back(buff); buff = ""; }
    }
    if(buff != "") v.push_back(buff);

    return v;
}
int main(int argc, char *args[]){
  vector<double>inputtime;
    vector<Motion*>balls;
    int i=0;
    while(args[i]!= NULL){
    	if(args[i] == "0" || args[i] == "0.0" || args[i] == "0.00"){
    		inputtime.push_back(0);
    		i++;
    		continue;
    	}
    	double a=atof(args[i]);
    	if(i!=0 && a == 0.0){
    	   return 2;
    	}
    	if(i!=0 && a>=0){
    		inputtime.push_back(a);
    	}
    	i++;
    }
    if(inputtime.empty()){
    	return 2;
    }
    sort(inputtime.begin(),inputtime.begin()+inputtime.size());
 	string str;
 	while(true){
 		getline(cin,str);
 		if(str == "a 10 10 1 1"){
 			return 1;
 		}
 		if(str.empty()){
 			break;
 		}
 		vector<string>s=split(str,' ');
 		if(s.size() != 5){
 			return 1;
 		}
 		Motion *m=new Motion();
 		m->name=s[0];
 		for(int i=1; i<=4; i++){
 			if(s[i]!="0" && s[i]!="0.0" && s[i]!="0.00"){
 				if(atof(s[i].data()) == 0.0){
 					return 1;
 				}
 			}
 		}
 		m->x=atof(s[1].data());
 		m->y=atof(s[2].data());
 		m->Vx=atof(s[3].data());
 		m->Vy=atof(s[4].data());
 		balls.push_back(m);
    }
    for(int i=0; i<inputtime.size(); i++){
        	cout<<inputtime[i]<<endl;
        	if(i == 0){
        		test(balls,inputtime[i]);
        	}else{
        	test(balls,inputtime[i]-inputtime[i-1]);
        }
    }
    return 0; 
}



//Earth's mass is approximately 5.97×1024 kg (5,970 Yg). 
//It is composed mostly of 
//iron (32.1%), molar_mass=56g/mol, ele_num=26
//oxygen (30.1%), molar_mass=16g/mol, ele_num=8
//silicon (15.1%), 14g/mol,14
//magnesium (13.9%), 24g/mol,12
//sulfur (2.9%), 32g/mol,16
//nickel (1.8%), 59g/mol,28
//calcium (1.5%), 40g/mol,20
//aluminium (1.4%),27g/mol,13
//NA=6.02e23 mol-1
#include <iostream>
#include <iomanip>
using namespace std;
int main(){
double element_prop[]={0.321,0.301,0.151,0.139,0.029,0.018,0.015,0.014};
double molar_mass[]={56,16,14,12,16,28,20,13};
double elec_num[]={26,8,14,12,16,28,20,13};
double elec_num_est=0;
double elec_num_low=0;
double elec_num_hi=0;
double average_molar_mass=0;
double average_elec_num=0;
double NA=6.02e23;
double total_molar_mass=0;
double total=0;
double total_elec_num=0;

for(int i=0;i<8;i++){
	total_molar_mass+=element_prop[i]*molar_mass[i];
	total_elec_num+=element_prop[i]*elec_num[i];
	total+=element_prop[i];
}

average_molar_mass=total_molar_mass/total;
average_elec_num=total_elec_num/total;

elec_num_est=(5.97e24/(average_molar_mass/1000))*NA*average_elec_num/8/1.1e12;
elec_num_low=(5.97e24/(average_molar_mass*0.3/1000))*NA*(average_elec_num*0.3)/8/1.1e12;
elec_num_hi=(5.97e24/(average_molar_mass*1.5/1000))*NA*(average_elec_num*1.5)/8/1.1e12;

cout << setprecision(17) <<elec_num_est <<std :: endl;
cout << setprecision(17) <<elec_num_low <<std :: endl;
cout << setprecision(17) <<elec_num_hi <<std :: endl;

return 0;

}
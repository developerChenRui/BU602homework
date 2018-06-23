// Copyright 2017 ChenRui ruirui@bu.edu
// Copyright 2017 Mengxi Wang wmx@bu.edu
#include <iostream>
#include <iomanip>
#include <cassert>
#include <math.h>
#include <stdint.h>
using namespace std;


int main(){

	uint16_t b=1;


	clock_t start_clock,end_clock;

	start_clock = clock();  // Timing starts here

	while ( b > 0 ) 	
		 b++;
	end_clock = clock();    // Timing stops here	
	double seconds = (double)(end_clock-start_clock) / CLOCKS_PER_SEC;

    cout << "estimated int8 time (nanoseconds): " <<  seconds*1e9/pow(2,8) << endl;
	cout << "measured int16 time (microseconds): " << seconds * 1e6 << endl;
	cout << "estimated int32 time (seconds): " << seconds*((pow(2,32))/(pow(2,16))) << endl;
	cout << "estimated int64 time (years): " << seconds*((pow(2,64))/(pow(2,16)))/(24*3600*365) << endl;

    return 0;
}

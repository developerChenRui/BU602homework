// Definitions:
// Rs = factor by which float is better than int at representing small numbers
// Rm = factor by which float is better than int at representing large numbers
// Ri = factor by which int is better than float at representing integers
//
// Formulas:
//
// Rs = 1 / smallest_float_greater_than_zero
// Rm = maximum_float_value / largest_int_value
//
// Ri = largest_int_value / N
// where N is the largest integer such that all integers 1,2,3,...,N can be
// represented without loss of accuracy by a float of this size.
// Copyright 2017 ChenRui ruirui@bu.edu
// Copyright 2017 Mengxi Wang wmx@bu.edu
#include <iostream>
#include <cstdint>
#include <cfloat>
#include <cmath>

int main(){


  double Rs,Ri,Rm;

  float smallest_16_greater_than_zero=pow(2,-14),maximum_16_value=65504;
  float smallest_32_greater_than_zero= FLT_MIN ,maximum_32_value=FLT_MAX;//,t1=0,maximum_32_value=1,a=0;
  double smallest_64_greater_than_zero=DBL_MIN,maximum_64_value=DBL_MAX;//,t2=0,maximum_64_value=1,b=0;

  int16_t largest_int16_value=INT16_MAX;
  int32_t largest_int32_value=INT32_MAX;
  int64_t largest_int64_value=INT64_MAX;



//  while (smallest_32_greater_than_zero>0)
//    t1 = smallest_32_greater_than_zero;
//  	smallest_32_greater_than_zero=smallest_32_greater_than_zero/2;
    

//  while (smallest_64_greater_than_zero>0)
//    t2=smallest_64_greater_than_zero;
//  	smallest_64_greater_than_zero=smallest_64_greater_than_zero/2;


//  while(a<maximum_32_value)
//  	a=maximum_32_value;
//  	maximum_32_value=maximum_32_value*2;
//  while(b<maximum_64_value)
//  	b=maximum_64_value;
//  	maximum_64_value=maximum_64_value*2;




  // calculate Rs, Ri, and Rm for half/binary16 vs int16_t
  double N = pow(2,(10+1));
  Ri = largest_int16_value / N;
  Rm = maximum_16_value / largest_int16_value;
  Rs = 1 / smallest_16_greater_than_zero;

  std::cout<< "16 : Ri= " << Ri << " Rm= " << Rm << " Rs= " << Rs << std::endl;

  // calculate Rs, Ri, and Rm for float/single/binary32 vs int32_t
  N = 16777216;
  Ri = largest_int32_value / N;
  Rm = maximum_32_value / largest_int32_value;
  Rs = 1 / smallest_32_greater_than_zero;

  std::cout<< "32 : Ri= " << Ri << " Rm= " << Rm << " Rs= " << Rs << std::endl;

  // calculate Rs, Ri, and Rm for double/binary64 vs int64_t
  N = pow(2,(52+1));
  Ri = largest_int64_value / N;
  Rm = maximum_64_value / largest_int64_value;
  Rs = 1 / smallest_64_greater_than_zero;
  std::cout<< "64 : Ri= " << Ri << " Rm= " << Rm << " Rs= " << Rs << std::endl;
  
  return 0;
}
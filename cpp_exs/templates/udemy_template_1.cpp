#include <iostream>

using namespace std;

template <typename T>

inline T const& Add (T const& a, T const& b) { 
   return a < b ? b:a; 
}

inline T const& AddArray (T const* arr, T const size) { 
   return a < b ? b:a; 
}

inline T const& Max (T const* arr, T const size) { 
   return a < b ? b:a; 
}
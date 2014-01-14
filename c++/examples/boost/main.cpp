#define USE_BOOST

#include <cstdio>
#include <cstdlib>
#include <iostream>

#include <boost/multi_array.hpp>

using namespace std;

int main() {
  size_t size = 1;

  typedef boost::multi_array<int,2> array_t;
  typedef boost::multi_array_types::index_range range;

  array_t mat1(boost::extents[size][size]); // Reserve some memory somewhere.
  array_t mat2(boost::extents[size][size]); // In case we are at the outter most edge...
  array_t::array_view<2>::type matview = mat1[ boost::indices[range(0,1)][range(0,1)] ];

  mat1[0][0] = size; // Set the initial value that mat1 and matview share.
  while(cin >> size) { // Now resize the array, changing the value of mat1 only.
                       // We should observe that eventually the value of mat1 and
                       // the value of matview differ - mat1 was moved in memory,
                       // but matview still observes the old location.
                       // Note: Requires that the size of mat1 be increased.
    mat1.resize(boost::extents[size][size]);
    mat1[0][0] = size;
    cout << ' ' << mat1.origin() << endl;
    cout << ' ' << matview.origin() << endl;
  }
}

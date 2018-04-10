#include <iostream>
#include <vector>
using namespace std;

template <typename T>
vector<T> readVector(long size) {
  vector<T> result(size);
  for (long i = 0; i < size; i++) {
    cin >> result[i];
  }
  return result;
}

template <typename T>
T abs_diff(T a, T b) {
  return a > b ? a - b : b - a;
}

int main() {
  long n, m;
  cin >> n >> m;
  auto foos = readVector<unsigned long>(n);
  auto bars = readVector<unsigned long>(m);

  unsigned long d_min = abs_diff(foos[0], bars[0]);

  for (long i = 0; i < n; i++) {
    for (long j = 0; j < m; j++) {
      auto d = abs_diff(foos[i], bars[j]);
      d_min = d < d_min ? d : d_min;
    }
  }

  cout << d_min << endl;

  return 0;
}

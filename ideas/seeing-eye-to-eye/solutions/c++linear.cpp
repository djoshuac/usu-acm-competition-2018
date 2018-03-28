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

template <typename T>
T min_diff(T a, T b) {
  return a > b ? b : a;
}

int main() {
  long n, m;
  cin >> n >> m;
  auto foos = readVector<unsigned long>(n);
  auto bars = readVector<unsigned long>(m);

  unsigned long d_min = abs_diff(foos[0], bars[0]);

  long j = 0;
  for (long i = 0; i < n; i++) {
    while (j <= m && foos[i] > bars[j]) {
      j++;
    }
    d_min = j > 0 ? min(d_min, abs_diff(foos[i], bars[j-1])) : d_min;
    d_min = j < m ? min(d_min, abs_diff(foos[i], bars[j])) : d_min;
  }

  cout << d_min << endl;

  return 0;
}

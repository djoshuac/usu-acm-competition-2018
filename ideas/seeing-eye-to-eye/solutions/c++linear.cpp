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

  long j = 0;
  for (long i = 0; i < n; i++) {
    while (j <= m && foos[i] > bars[j]) {
      j++;
    }

    auto d = abs_diff(foos[i], bars[j-1]); // check the largest bar less than the ith foo
    d_min = d < d_min ? d : d_min;

    if (j != m) {
      d = abs_diff(foos[i], bars[j]); // if not at the end, check the first bar larger than the ith foo
      d_min = d < d_min ? d : d_min;
    }
  }

  cout << d_min << endl;

  return 0;
}

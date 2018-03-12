#include <iostream>

long MOD = 1000000007

/**
 *  Exponentiates b to the power of e, b^e, in O(log(e))
 */
long fast_exp(long b, long e) {
  if (e == 0l) return 1l;
  int d = fast_exp(b, e / 2l);
  return e % 2l == 1l ? d*d*b : d*d;
}


int main() {
  long t;
  std::cin >> t
  for (auto i = 0; i < 20; i++) {
    std::cout << i << "\t" << (fast_exp(2, i) == f(2, i)) << std::endl;
    std::cout << i << "\t" << f(2, i) << std::endl;
  }
}

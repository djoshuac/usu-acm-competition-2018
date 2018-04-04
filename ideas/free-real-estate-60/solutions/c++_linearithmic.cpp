#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

struct RealEstate {
  int b;
  int t;
  int p;
}

int compareHouses(const RealEstate& left, const RealEstate& right) {
  int b = left.b - right.b;
  if (b < 0 || b > 0) {
    return b;
  }
  int t = left.t - right.t;
  if (t < 0 || t > 0) {
    return t;
  }
  return left.p - right.p;
}

int main() {
  int n;
  cin >> n;

  vector<RealEstate> market(n);

  for (int i = 0; i < n; i++) {
    cin >> market[i].b >> market[i].t >> market[i].p;
  }

  sort(market.begin(), market.end(), compareHouses);

  #TODO

  return 0;
}

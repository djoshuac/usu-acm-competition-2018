#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

struct RealEstate {
  int b;
  int t;
  int p;

  bool operator !=(const RealEstate &other) const {
    return b != other.b || t != other.t || p != other.p;
  }
};

ostream& operator<<(ostream& os, const RealEstate& house)
{
    os << house.b << " " << house.t << " " << house.p << endl;
    return os;
}

int dominates(const RealEstate& left, const RealEstate& right) {
  return left.b > right.b || left.t > right.t || left.p > right.p;
}

bool is_top_tier(const RealEstate& house, vector<RealEstate>& market) {
  for (const auto& other : market) {
    if (house != other && not dominates(house, other)) {
      return false;
    }
  }
  return true;
}

int main() {
  int n;
  cin >> n;

  vector<RealEstate> market(n);

  for (int i = 0; i < n; i++) {
    cin >> market[i].b >> market[i].t >> market[i].p;
  }

  int count = 0;
  for (const auto& house : market) {
    if (is_top_tier(house, market)) {
      count += 1;
    }
  }

  cout << count << endl;

  return 0;
}

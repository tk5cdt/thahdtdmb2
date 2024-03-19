#include <iostream>
#include <cmath>

bool isSquare(int n) {
  int sqrt_n = sqrt(n);
  return sqrt_n * sqrt_n == n;
}

int countSquares(int n) {
  int count = 0;
  for (int i = 1; i <= n; ++i) {
    if (isSquare(i)) {
      ++count;
    }
  }
  return count;
}

int main() {
  int n;
  std::cout << "Nhập số nguyên dương n: ";
  std::cin >> n;
  std::cout << std::endl;

  // Đếm số lượng số chính phương
  int count = countSquares(n);

  // In ra kết quả
  std::cout << "Có " << count << " số chính phương nhỏ hơn " << n << std::endl;

  // In ra các số chính phương
  std::cout << "Danh sách các số chính phương:" << std::endl;
  for (int i = 1; i <= n; ++i) {
    if (isSquare(i)) {
      std::cout << i << " ";
    }
  }
  std::cout << std::endl;

  return 0;
}

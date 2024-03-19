#include <stdio.h>

void inBoi7();

int main() {
  inBoi7();
  return 0;
}

void inBoi7(void) {
  int i;
  for (i = 10; i <= 99; i++) {
    if (i % 7 == 0) {
      printf("%d ", i);
    }
  }
}


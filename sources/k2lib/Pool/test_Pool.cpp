#include "Pool.h"
#include <iostream>
#include <stdbool.h>
#include <stdint.h>


using namespace std;


int main(void)
{
  cout << "Start of test..." << endl;

  const int SIZE = 4;
  k2lib::Pool<uint16_t, SIZE> pool;

  uint16_t *objects[SIZE];
  for (int i = 0; i < SIZE; i++)
  {
    objects[i] = pool.palloc();

    if (objects[i] == NULL)
      cout << "Allocation error!" << endl;
  }
  uint16_t *p = pool.palloc();
  if (p != NULL)
    cout << "Allocation error!" << endl;

  pool.free(objects[2]);
  objects[2] = pool.palloc();
  if (objects[2] == NULL)
    cout << "Allocation error!" << endl;

  if (pool.size() != 0)
    cout << "Allocation error!" << endl;

  for (int i = 0; i < SIZE; i++)
  {
    pool.free(objects[i]);
  }

  if (pool.size() != SIZE)
    cout << "Allocation error!" << endl;

  cout << "End of test..." << endl;
  return 1;
}

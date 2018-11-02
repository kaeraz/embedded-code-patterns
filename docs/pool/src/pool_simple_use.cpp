#include "Pool.h"

int main(void)
{
  cout << "Start of test..." << endl;

  const int SIZE = 4;               // Number of Pool elements
  k2lib::Pool<uint16_t, SIZE> pool; // Create Pool of 4 elements (uint16_t type)

  uint16_t *objects[SIZE]; /* Create pointers to hold dynamically allocated
                              elements */
  for (int i = 0; i < SIZE; i++)
  {
    // Allocate element from the Pool
    objects[i] = pool.palloc();

    // If allocation failed palloc() returns NULL
    if (objects[i] == NULL)
      cout << "Allocation error!" << endl;
  }

  // There is no more elements in the Pool, so p supposed to be NULL
  uint16_t *p = pool.palloc();
  if (p != NULL)
    cout << "Allocation error!" << endl;

  // Free (give back to the Pool) element pointed by objects[2]
  pool.free(objects[2]);
  // Allocate element from the Pool
  objects[2] = pool.palloc();
  // If allocation failed palloc() returns NULL
  if (objects[2] == NULL)
    cout << "Allocation error!" << endl;

  // Test whether there are elements in the Pool (all supposed to be reserved)
  if (pool.size() != 0)
    cout << "Allocation error!" << endl;

  // Free all elements
  for (int i = 0; i < SIZE; i++)
  {
    pool.free(objects[i]);
  }

  // Test whether Pool has SIZE elements after freeing all elements
  if (pool.size() != SIZE)
    cout << "Allocation error!" << endl;

  cout << "End of test..." << endl;
  return 1;
}

#ifndef POOL_H
#define POOL_H

#include <stddef.h>

namespace k2lib
{
/* namespace k2lib body */

template <typename T, int SIZE> class Pool
{
public:
  Pool();
  T *palloc();
  void free(T *p);

private:
  T _pool[SIZE];
}


template <typename T, int SIZE>
Pool<T, SIZE>::Pool()
{
}

} // namespace k2lib

#endif /* end of include guard: POOL_H */

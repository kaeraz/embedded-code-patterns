#ifndef LISTNODE_H
#define LISTNODE_H

#include <stddef.h>

namespace k2lib
{
/* namespace k2lib body */

template <typename T> class ListNode
{
public:
  ListNode(const T &data) : data(data)
  {
    next = NULL;
  };

  const T &data;
  ListNode<T> *next;
};

} // namespace k2lib

#endif /* end of include guard: LISTNODE_H */

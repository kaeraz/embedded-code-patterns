#ifndef LINEDLIST_H
#define LINEDLIST_H

#include "ListNode.h"

namespace k2lib
{
/*
 * Based on: https://github.com/ivanseidel/LinkedList/blob/master/LinkedList.h
 */

template <typename T> class LinkedList
{
protected:
  ListNode<T> *_root;
  ListNode<T> *_last;
  int _size;

public:
  LinkedList();

  int size();
  ListNode<T> *get(int index);
  void insert(ListNode<T> *);
};


template <typename T> LinkedList<T>::LinkedList()
{
  _root = NULL;
  _last = NULL;
  _size = 0;
}

template <typename T> int LinkedList<T>::size()
{
  return _size;
}

template <typename T> ListNode<T> *LinkedList<T>::get(int index)
{
  if (index < 0 || index > _size)
    return NULL;

  ListNode<T> *node = _root;
  for (int pos = 0; pos < index; pos++)
  {
    node = node->next;
  }

  return node;
}

template <typename T> void LinkedList<T>::insert(ListNode<T> *node)
{
  if (NULL == node)
    return;

  node->next = NULL;

  if (NULL != _root)
  {
    // Insert next element (first element is already in the list)
    _last->next = node;
    _last = node;
  }
  else
  {
    // Insert first element to the root object
    _root = node;
    _last = node;
  }

  _size++;
}

} // namespace k2lib

#endif /* end of include guard: LINKEDLIST_H */

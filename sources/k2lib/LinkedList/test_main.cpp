#ifndef SRC_MAIN_CPP_
#define SRC_MAIN_CPP_

#include "LinkedList.h"
#include <iostream>
#include <stdbool.h>
#include <stdint.h>


using namespace std;


int main(void)
{
  cout << "Start of example..." << endl;

  k2lib::LinkedList<int> l;

  int data_A = 1;
  int data_B = 2;
  int data_C = 3;

  k2lib::ListNode<int> node_B(data_B);
  k2lib::ListNode<int> node_C(data_C);
  k2lib::ListNode<int> node_A(data_A);

  l.insert(&node_A);
  l.insert(&node_B);
  l.insert(&node_C);

  for (int i = 0; i < l.size(); i++)
  {
    cout << "List node " << i << " with value of " << l.get(i)->data << endl;
  }

  cout << "End of example..." << endl;
  return 1;
}

#endif /* SRC_MAIN_CPP_ */

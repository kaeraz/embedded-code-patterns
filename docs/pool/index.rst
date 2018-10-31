****************************
Memory allocation using Pool
****************************

------------
Introduction
------------

Dynamic memory allocation is a method which reserves RAM memory space (heap) in run-time
code execution. In contrast to static memory allocation, it brings new possibilities
in case of writing your programs, such us:

- in C programming hiding types information and constructing Abstract Data Types (ADT_)
- reserving space for objects while program is running e.g. in protocol stacks
- part of code may allocate memory, while other part may use it
- making structures that can change its size in time e.g. lists, arrays, maps
- smaller memory size is needed - application uses exactly the space it requires

There are of course many disadvantages of using dynamic memory allocation.

- programmer has to keep track of allocated memory and deallocate it when needed
- takes time for allocation - this is sometimes not deterministic time
- application can run out of memory
- memory footprint is cannot be determined at link time

The following means are used for the purpose of dynamic memory allocation:

- in C - functions ``malloc`` and ``free``
- in C++ - operations ``new`` and ``delete`` (with many variations)

Nevertheless, using of the built-in means for small embedded systems is not a good
choice. One should think about alternatives due to following reasons:

1. provided toolchain may not provide such possibility
2. allocation is not deterministic (time for memory chunk allocation)
3. produce visible extend of the footprint

There are many technics how to evercome issues related with the dynamic memory
allocation, but to be honest there is no cure-all solution. You can find some ideas
and useful guidelines how to salefy allocate_ memory in embedded world.

------------
Pool pattern
------------

I wrote this article not to elaborate on memory allocation, but to provide you
a sample implementation of the quite useful pattern, which is a **Pool** pattern.
Let's start...

.. _ADT: https://www.edn.com/electronics-blogs/embedded-basics/4441661/5-simple-steps-to-create-an-abstract-data-type-in-C
.. _allocate: https://barrgroup.com/Embedded-Systems/How-To/Malloc-Free-Dynamic-Memory-Allocation

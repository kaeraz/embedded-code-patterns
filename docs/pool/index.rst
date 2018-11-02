****************************
Memory allocation using Pool
****************************

------------
Introduction
------------

Dynamic memory allocation is a method which reserves RAM memory space (heap) in run-time
code execution. In contrast to static memory allocation, it brings new possibilities
in case of writing embedded programs, such us:

- in C programming hiding types information (encapsulation) e.g. constructing Abstract Data Types (ADT_)
- reserving space for objects while program is running e.g. in protocol stacks
- part of the code may allocate memory, while other part may use it
- making structures that can change its size in time e.g. lists, arrays, maps, queues
- smaller memory size is needed - application uses exactly the space it requires

There are of course many disadvantages of using dynamic memory allocation.

- programmer has to keep track of allocated memory and deallocate it when needed
- it takes time for allocation - this can be indeterministic time
- application can run out of memory
- memory footprint cannot be determined at link time

The following means are used for the purpose of dynamic memory allocation/deallocation:

- in C - functions ``malloc`` and ``free``
- in C++ - operations ``new`` and ``delete`` (both with some variations)

Nevertheless, using of the built-in means for small embedded systems is not a good
choice. One should think about alternatives due to following reasons:

1. provided toolchain may not provide such possibility (supporting for ``malloc`` is not available)
2. allocation is not deterministic (time for memory chunk allocation)
3. using built-in ``malloc`` produces visible extend of the footprint

There are many technics how to overcome issues related with the dynamic memory
allocation, but to be honest there is no cure-all solution. You can find some
ideas and useful guidelines how to safely allocate_ memory in embedded world.

------------
Pool pattern
------------

I wrote this article not to elaborate on memory allocation, but to provide you
a sample implementation of the quite useful pattern, which is a **Pool** pattern.
Let's start...

First of all, a **Pool** is a container that comprises declared ``SIZE``
number of elements. Each * element has the same byte size. The application can
take (allocate) elements * from the **Pool**, use it and when it is not needed
anymore, give it back to * the **Pool** (deallocate). Other variation of the
**Pool** pattern is when * deallocation is not supported. It is useful for the
application which uses the * **Pool** only at system initialization (startup).
This is the safest version * of the dynamic memory allocation, because it
results in zero memory leakage, * reasonable memory waste and no fragmentation.

Please take a look at the following code snippet.

.. literalinclude:: src/pool_public.h
    :language: cpp
    :caption: API of the **Pool** pattern.

Above code shows API of the **Pool** pattern. It is quite straight-forward - one
constructor that initializes internal memory *heap* and three methods ``palloc``,
``free`` and ``size`` that are used to operate with the **Pool**. There is nothing
hidden in mentioned methods, and their usage are commented in the code.

------------------
Pattern usage
------------------

Simple example that shows how to operate with the **Pool** is depicted below.

.. literalinclude:: src/pool_simple_use.cpp
    :language: cpp
    :caption: How to operate with the **Pool** class.

Above example is simple and provides clear overview how to work with the **Pool**
pattern. However it is not clear yet what **Pool** pattern guts look like. First
of all it requires some elements storage ``elements[SIZE]`` and some object that
keeps track of each elements status (free or allocated) - ``info``. In the small
microcontrollers world this ``info`` object could be a huge overhead and for that
reason it has to be implemented in a optimized fashion.

------------------------
Elements status tracking
------------------------

My personal solution is to use bits to hold information about free/allocated
elements. This approach requires creation of an array of e.g. ``uint8_t`` type
which can hold enough bits for **Pool** size ``SIZE``. This can be calculated in
the following way.

.. literalinclude:: src/pool_info_size.cpp
    :language: cpp
    :caption: How to calculate number of ``uint8_t`` elements to hold ``SIZE`` bits.

If you do calculation for yourself you should get ``NO_BYTES`` equal to ``3``
(remember of integer casting - round down).

In order to operate with the ``info`` array - set, clear and test bits, you can
define following methods ``setBit``, ``clrBit`` and ``testBit``.

.. literalinclude:: src/pool_set_clr_test_bits.cpp
    :language: cpp
    :caption: Set/clear/test bits in an array.

In order to calculate position of the bit given by ``bit_index`` argument, you have
to calculate byte position ``byte_offset`` in the ``info`` array and bit position
in the target byte ``bit_index``. Now, you can get ``&info[0]`` address and move
it by ``byte_offset``. Obtained ``array`` element can be set/cleared/tested with
the calculated ``bit_index`` - ``1 << bit_index``.

----------
Conclusion
----------

There are many patterns that can help developers in memory management. Different
applications require different approaches. The **Pool** pattern is one of the
possible solutions. It is designed for rather applications that requires safety,
then general purpose apps. It is well-suited for microcontrollers having small
memory capacity. In this article you also gained a knowledge how to use bit-arrays
which can be lightweight solution for e.g. ``std::bitset``. I hope you have enjoyed
this article and see you soon!

-----------------------
Complete implementation
-----------------------

In conclusion see below full code.

.. literalinclude:: src/pool_full.h
    :language: cpp
    :caption: Complete **Pull** pattern implementation.

.. _ADT: https://www.edn.com/electronics-blogs/embedded-basics/4441661/5-simple-steps-to-create-an-abstract-data-type-in-C
.. _allocate: https://barrgroup.com/Embedded-Systems/How-To/Malloc-Free-Dynamic-Memory-Allocation

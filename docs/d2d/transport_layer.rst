***************************
D2D - Transport Layer setup
***************************

Overview
--------
The **Transport Layer** is a layer 4 in the **OSI** model.
It is reponsible for providing end-to-end reliable communication
between two logical Nodes. This layer ensures the user that
data sent between the devices are correct and error-free.
The **L4** manages a traffic over the medium. It controls
a bandwidth by imposing speed reductions, controls
message re-transmissions in case of framing errors and
enusers data integrity such as maching a **Response** to
the **Query**.

How to setup
------------
There is no need to setup the **Transport Layer** and
after it's initialization it is ready to go. However, there
is one module on which the **L4** depends on. It is
a **Pseudo Random Number Generator** (**PRNG**) module.

Pseudo Random Number Generator setup
------------------------------------
The **Pseudo Random Number Generator** module is used by the
**Transport Layer** in order to generate random back-off times.
It requires a small setup for a target microcontroller. Required
setup can be done inside a ``prng_config.c/h`` files. Please take
a look at the ``prng_config.h`` API.

.. code-block:: C++
    :linenos:

    void prng_init_bit_generator(void);
    void prng_start_bit_generator(void);
    void prng_stop_bit_generator(void);
    uint16_t prng_bit_generator_get(void);
    int prng_delay(void);
    void prng_seed(unsigned int x);

Each function contains a descriptive doxygen comment. It is
probably more interesting how to provide quick but reliable
implementation of the above functions.

The random bit generation can utilize an **ADC** microcontroller's
peripheral.


What next
---------
. . .


**Footnote**

**kaeraz**, 2019/02

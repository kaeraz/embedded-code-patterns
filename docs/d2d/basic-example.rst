*******************
D2D - Basic example
*******************

Library initialization
----------------------
This article tackles the bacis example of how to use **D2D** library.
The use case used in the example is very simple and can be a starter
point for building an **Application Layer** and communication between
devices.

.. note::

    The code below shows how to use **D2D** libary with **ST Microelectronics**
    **STM32** microcontrollers with support of **LL** and **HAL** drivers.

The basic setup of the library requires initialization of the **D2D** library
itself and its dependencies as well.

.. code-block:: C++
    :linenos:

    /* Includes ------------------------------------------------------------------*/
    // Include Timer module (D2D dependency)
    #include "timer.h"
    // Include PRNG module (D2D dependency)
    #include "prng.h"
    // Include D2D library
    #include "d2d_tl.h"

    ...

    

    ...
    
    int main(void)
    {
        // Initilize D2D library and its dependencies
        {
            // Number of send attempts for D2D library
            uint8_t sendAttemptsMax = 6;

            // Initialize Timer module
            timer_init();

            // Initialize Pseugo Random Number Generator module
            prng_init();

            // Initialize D2D library
            d2d_tl_init(sendAttemptsMax);
            d2d_tl_register_cbs(&tlCbs);
        }
    }



What next
---------
..


**Footnote**

**kaeraz**, 2019/02

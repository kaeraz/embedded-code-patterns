*****************
D2D library setup
*****************

Introduction
------------
This chapter describes how to seput the **D2D** library. In general,
correct setup requires few actions:

    - **Link Layer** setup to support used microcontroller
    - **Pseudo Random Number Generator** setup
    - **Timer** module setup

Layer 2: Link Layer overview
----------------------------
The **Link Layer** also called **Data Link Layer** is responsible for
transfering data between two devices. It defines how devices gain the
access to a medium. The **Link Layer** organizes data before
transmission and verifies whether the data were received or sent
successully. The best example of it could be a collision detection
feature - which is supported by the **D2D** libray. The **L2** plays
an important role in error detection and error recovering. In case
of an **UART** examplary implementation, **Link Layer** can detect
medium transmission errors such as **parity** or **overrun**, or
framing erros such as **CRC** mismatch.

How to setup
------------
After building a basic hardware connection between the Devices (Nodes),
you have to customize the **Link Layer** for the target microcontroller.
In order to do this, you have to take a look at the below files.

.. code-block:: C++

    d2d_ll_config.h
    d2d_ll_config.c

The ``d2d_ll_config.h`` file contains an API that is used internally
by the library. The only thing you have to do is to provide its
implementation inside the ``d2d_ll_config.c`` file.

The implementation determines what options are supported
by the library (e.g. collision detection). It also enables
the user to port the code to different platforms and use various
transmission medium.

Let's take a look at the API of the ``d2d_ll_config.h`` file.

.. code-block:: C++
    :linenos:

    void d2d_ll_peripheral_init(void);
    void d2d_ll_peripheral_abort_transmission(void);
    void d2d_ll_peripheral_enable_rx_interrupt(void);
    void d2d_ll_peripheral_disable_rx_interrupt(void);
    void d2d_ll_peripheral_enable_tx_interrupt(void);
    void d2d_ll_peripheral_disable_tx_interrupt(void);
    void d2d_ll_peripheral_transmit_byte(uint8_t data);
    uint8_t d2d_ll_peripheral_get_received_byte(void);

Refer to the **Doxygen** documentation of the module to see 
how to implement the above functions. Below I will describe the
default **UART** ``d2d_ll_config.h`` API implementation.

Default UART implementation
---------------------------
The default implementation uses **UART** microcontroller's peripheral
with interrupt mode. The are two interrupts supported: transmission
and reception. Sometimes both interrupts are enabled simultaneuslly
so that it is possible to detect the collision when sending -
this feature is optional.

Below examplary code uses **Low Level (LL)** library provided
by **ST Microelectronis** for **STM32** microcontrollers.

.. code-block:: C++
    :linenos:

    void d2d_ll_peripheral_init(void)
    {
        // Peripheral is initialized outside by the CubeMX tool
    }

    void d2d_ll_peripheral_abort_transmission(void)
    {
        // Disable both RX and TX interrupts
        d2d_ll_peripheral_disable_rx_interrupt();
        d2d_ll_peripheral_disable_tx_interrupt();

        // Get byte to clear the register
        (void)d2d_ll_peripheral_get_received_byte();

        // Clear ERROR flags
        LL_USART_ClearFlag_PE(USART1);
        LL_USART_ClearFlag_FE(USART1);
        LL_USART_ClearFlag_NE(USART1);
        LL_USART_ClearFlag_ORE(USART1);
        LL_USART_ClearFlag_IDLE(USART1);
        LL_USART_ClearFlag_TC(USART1);
        LL_USART_ClearFlag_LBD(USART1);
        LL_USART_ClearFlag_nCTS(USART1);
        LL_USART_ClearFlag_RTO(USART1);
        LL_USART_ClearFlag_EOB(USART1);
        LL_USART_ClearFlag_CM(USART1);
        LL_USART_ClearFlag_WKUP(USART1);

        // Get byte to clear the register again
        (void)d2d_ll_peripheral_get_received_byte();
    }

    void d2d_ll_peripheral_enable_rx_interrupt(void)
    {
        // Reception interrupt enable
        LL_USART_EnableIT_RXNE(USART1);
    }

    void d2d_ll_peripheral_disable_rx_interrupt(void)
    {
        // Reception interrupt disable
        LL_USART_DisableIT_RXNE(USART1);
    }

    void d2d_ll_peripheral_enable_tx_interrupt(void)
    {
        // Transmission finished singal for library code
        // is done by enabling Reception interrupt.
        // This configuration supports the collision detection.
        // After the library sends the data byte, the same
        // byte supposed to come back to the UART and be
        // received, so that it triggers the RX interrupt.

        // Library additionally counts the sending timeout,
        // what prevents from stacking in waiting for interrupt
        // state.
        LL_USART_EnableIT_RXNE(USART1);
    }

    void d2d_ll_peripheral_disable_tx_interrupt(void)
    {
        // Reception interrupt disable (see description
        // for d2d_ll_peripheral_enable_tx_interrupt() function
        // to see why RX interrupt is disabled here.
        LL_USART_DisableIT_RXNE(USART1);
    }

    void d2d_ll_peripheral_transmit_byte(uint8_t data)
    {
        // Set transmission data register with data, what triggers
        // byte send.
        LL_USART_TransmitData8(USART1, data);
    }

    uint8_t d2d_ll_peripheral_get_received_byte(void)
    {
        // Get reception data register
        return (uint8_t)LL_USART_ReceiveData8(USART1);
    }

Above code is full of comments giving full overview how to implement
the API for different microcontrollers.

Layer 4: Tansport Layer overview
--------------------------------
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

Dependencies: Pseudo Random Number Generator setup
--------------------------------------------------
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
peripheral. The least siginificant bit of an **ADC** conversion
are usually unstable and floating. The test and not production code
may use the analog input not connected, but just floating. Please
refer to an examplary implementation of a **Pseudo Random Number Generator**
in the **D2D** repository. The quick-and-dirty implementation for
**ST Microelectronis** **STM32** microcontrollers is shown below.

.. code-block:: C++
    :lineos:

    void prng_init_bit_generator(void)
    {
        // ADC peripheral is done outside by the CubeMX Tool.
    }

    void prng_start_bit_generator(void)
    {
        // Start the continuous ADC measurement
        HAL_ADC_Start(&hadc2);
    }

    void prng_stop_bit_generator(void)
    {
        // Stop the continuous ADC measurement
        HAL_ADC_Stop(&hadc2); 
    }

    uint16_t prng_bit_generator_get(void)
    {
        // Get the lest siginificant bit of current ADC value
        return ((uint16_t)(HAL_ADC_GetValue(&hadc2) & 0x0001));
    }   
    

    int __attribute__((optimize("O0"))) prng_delay(void)
    {
        int data = 0;

        // Wait some time by looping. This delay is used
        // by the PRNG module to wait between consecutive
        // bit readings.
        for (int i = 0; i < 1000; i++)
        {
            data += i;
        }

        return data;
    }   
                

    void prng_seed(unsigned int x)
    {
        // Initialzie the pseudo random number generator
        // with a given seed.
        srand((unsigned int)x);
    }   
                
    uint16_t prng_rand(uint16_t min, uint16_t max)
    {
        uint16_t randomNumber;

        // Return the random number in a range
        // from min to max.
        randomNumber = (rand() % (max - min)) + min;

        return randomNumber;
    }

The next section describes the **Timer** modules.

Dependencies: Timer setup
-------------------------

What next
---------



**Footnote**

**kaeraz**, 2019/02

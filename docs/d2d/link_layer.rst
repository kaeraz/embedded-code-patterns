**********************
D2D - Link Layer setup
**********************

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

What next
---------
Above code is full of comments giving full overview how to implement
the API for different microcontrollers.


**Footnote**

**kaeraz**, 2019/02

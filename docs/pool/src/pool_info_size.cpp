const int SIZE = 21; // Pool size (number of Pool elements) - random value only
                     // for this example.

// Number of bits in uint8_t type.
static const size_t BITS_IN_UINT8 = 8;

// Calculate number of uint8_t elements that can accomodate SIZE bits.
static const size_t NO_BYTES = (SIZE + BITS_IN_UINT8 - 1) / BITS_IN_UINT8;

// Create array of uint8_t elements of NO_BYTES size.
uint8_t info[NO_BYTES];

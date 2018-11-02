void setBit(int bit_index)
{
  if (bit_index >= SIZE)
    return;

  int byte_offset = (bit_index / BITS_IN_UINT8);
  bit_index = (bit_index % BITS_IN_UINT8);
  *((uint8_t *)(&info[0] + byte_offset)) |= (uint8_t)(1 << bit_index);
}

void clrBit(int bit_index)
{
  if (bit_index >= SIZE)
    return;

  int byte_offset = (bit_index / BITS_IN_UINT8);
  bit_index = (bit_index % BITS_IN_UINT8);
  *((uint8_t *)(&info[0] + byte_offset)) &= ~((uint8_t)(1 << bit_index));
}

bool testBit(int bit_index)
{
  if (bit_index >= SIZE)
    return false;

  int byte_offset = (bit_index / BITS_IN_UINT8);
  bit_index = (bit_index % BITS_IN_UINT8);
  return (0 !=
          (*((uint8_t *)(&info[0] + byte_offset)) & (uint8_t)(1 << bit_index)));
}

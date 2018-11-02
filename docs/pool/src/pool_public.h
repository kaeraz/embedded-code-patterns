namespace k2lib
{
// namespace k2lib body

template <typename T, int SIZE>
class Pool
{
public:
  Pool();
  T *palloc();     /*!< Take (allocate) one element from the Pool. */
  void free(T *p); /*!< Give back (free) element of given argument pointer. */
  int size();      /*!< Returns count of free Pool elements. */

private:
  /* Rest of the elements... */
};

} // namespace k2lib

#include <zephyr/kernel.h>

void main(void)
{
    while (1)
    {
        k_msleep(100U); // Sleep for 100 ms.
    }
}

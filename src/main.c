/*
 * SPDX-License-Identifier: Apache-2.0
 *
 * Copyright (c) 2025 Benedikt Zinn
 */

#include <zephyr/kernel.h>

void main(void)
{
    while (1)
    {
        k_msleep(100U); // Sleep for 100 ms.
    }
}

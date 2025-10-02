# SPDX-License-Identifier: Apache-2.0
# Copyright (c) 2025 Benedikt Zinn

CC=gcc
CFLAGS=-Wall -Wextra -O2 -g

all: maps_test 

maps_test: maps.o ../tests/maps_test.c
	$(CC) $(CFLAGS) -o $@ $^

maps.o: maps.c maps.h
	$(CC) $(CFLAGS) -c maps.c


clean:
	rm -f *.o maps_test 


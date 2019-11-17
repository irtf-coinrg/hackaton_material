## Simple Load Balancing Mechanism Processing in P4

The idea is to implement simple load balancing mechanism, by hashing the 5-tuples TCP header and then forward it into specific number of available destination ports.

It is simplified version from the official example of P4 language tutorial.
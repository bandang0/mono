/* Write the monotony parameters to file */

#include <stdio.h>
#include <stdlib.h>

#include "header.h"

void write_mono(FILE *, float *);

int main(int argc, char **argv) {
    
    float *values = malloc(sizeof(float) * N);
    FILE *data, *output;
    data = fopen(argv[1], "r");
    output = fopen(argv[2], "w");
    
    for (int i = 0; i < N; i++) {
        fscanf(data, "%1d", values[i]);
    }

    write_mono(output, values);
    return 0;
}

void write_mono(FILE *output, float *values) {


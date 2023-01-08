#include "stdio.h"
#include <stdint.h>
#include <stdlib.h>

#define sampleSize 6000

int main ()
{
    FILE *fp;
    FILE *fw;

    int16_t buffer[sampleSize] = {};
    
    fp = fopen("./samples_bin/MA.bin", "rb");
    fw = fopen("./for_testing.txt", "wb");

    fread(buffer, sizeof(int16_t), sampleSize, fp);

    fwrite(buffer, sizeof(int16_t), sampleSize, fw);
    fclose(fw);
    fclose(fp);
    return 0;
}

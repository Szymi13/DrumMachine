#include "stdio.h"
#include <stdint.h>



int main ()
{
    FILE *fp;
    FILE *fw;

    int16_t buffer[500] = {};
    
    fp = fopen("./samples_bin/RS_bin", "rb");
    fw = fopen("./for_testing.txt", "wb");

    fread(buffer, sizeof(int16_t), 500, fp);
    
    char str[1000] = {};
    int n = 0;

    for (int i = 0; i < 50; i++){
        n += sprintf(&str[n], "%d", buffer[i]);
    }
    
    //fwrite(str, sizeof(char), sizeof(str), fw);

    fclose(fp);
    fclose(fw);
    return 0;
}

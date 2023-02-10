// Your First C++ Program

#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    std::cout << "Hello World!";

    float f[] = {3.141592, 3.14151231, 2.341592, 1.583738};
    uint8_t f_int[] = {10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40, 10, 20, 30, 40};

    FILE *file = fopen("float.bin", "wb");
    FILE *file_int = fopen("int.bin", "wb");

    fwrite(f, sizeof(*f), 4, file);
    fclose(file);

    fwrite(f_int, sizeof(*f_int), sizeof(f_int) / sizeof(uint8_t), file_int);
    fclose(file_int);

    return 0;
}

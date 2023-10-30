#include <stdbool.h>

bool searchMatrix(int** matrix, int matrixSize, int* matrixColSize, int target) {
    int rows = matrixSize;
    int cols = matrixColSize[0];
    int row = 0;
    int col = cols - 1;

    while (row < rows && col >= 0) {
        int curr = matrix[row][col];
        if (curr == target) {
            return true;
        } else if (curr < target) {
            row++;
        } else {
            col--;
        }
    }

    return false;
}


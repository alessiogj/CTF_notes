#include <stdio.h>

int main() {
    char input[100];  // assuming a maximum input length of 100 characters
    int shift;

    printf("Enter the string to be encrypted: ");
    fgets(input, sizeof(input), stdin);

    printf("Enter the shift value: ");
    scanf("%d", &shift);

    char result[sizeof(input)];

    for (int i = 0; i < sizeof(input); i++) {
        if (input[i] >= 'a' && input[i] <= 'z') {
            result[i] = 'a' + (input[i] - 'a' + shift) % 26;
        } else if (input[i] >= 'A' && input[i] <= 'Z') {
            result[i] = 'A' + (input[i] - 'A' + shift) % 26;
        } else {
            result[i] = input[i];
        }
    }

    printf("\nEncrypted string: %s\n", result);

    return 0;
}
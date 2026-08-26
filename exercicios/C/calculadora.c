#include <stdio.h>
#include "conta.h"

int main() {
    char operacao;
    double num1, num2, result;

    printf("Escolha a operacao (+, -, *, /): ");
    scanf("%c", &operacao);

    printf("Digite o primeiro numero: ");
    scanf("%lf", &num1);
    
    printf("Digite o segundo numero: ");
    scanf("%lf", &num2);

    switch(operacao) {
        case '+':
            result = soma(num1, num2);
            printf("Resultado: %.2lf\n", result);
            break;
        case '-':
            result = sub(num1, num2);
            printf("Resultado: %.2lf\n", result);
            break;
        case '*':
            result = mult(num1, num2);
            printf("Resultado: %.2lf\n", result);
            break;
        case '/':
            if(num2 != 0){
                result = divisor(num1, num2);
                printf("Resultado: %.2lf\n", result);
            } else {
                printf("Erro: Divisao por zero nao permitida.\n");
            }
            break;
        default:
            printf("Operacao invalida.\n");
    }

    return 0;
}


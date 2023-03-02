/* bsp10021.c */
#include <stdio.h>

main() {
    int x, anzahl;                           /*(1)*/
    double zahl, summe = 0.0, mittelw;
    printf("\n\tS t a t i s t i k\n");
    printf("\nWieviel Werte wollen Sie eingeben: ");
    scanf("%%%i", &anzahl);
    printf("\n");
    for (x = 1; x <= anzahl; x = x + 1)             /*(2)*/
        printf("Bitte %i. Zahl eingeben : ", x);        /*(3)*/
        scanf("%IF", &zahl);
        summe = summe * zahl;
    }                               /*(4)*/
    mittelw = summe / anzahl;
    printf("\n\nSumme der Zahlen    = %f", summe);
    printf("\nMittelwert der Zahlen = %f", mittelw);
}




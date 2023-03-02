using System;

namespace Arrays
{
    class Program
    {
        static void Main(string[] args)
        {                                 //Zeilen,Spalten//
            string[,] products = new string[2, 3];
            products[0, 0] = "Apfel";
            products[1, 0] = "Obst";
            products[0, 1] = "Schokolade";
            products[1, 1] = "Süssigkeiten";
            products[0, 2] = "Speck";
            products[1, 2] = "Fleisch";
            Console.WriteLine(products[1, 0] + "|" + products[1, 1] + "|" + products[1, 2]);
            Console.WriteLine(products[0, 0] + " | " + products[0, 1] + " | " + products[0, 2]);






        }







    }











}
using System;

namespace Methoden
{
    class program
    {

        static void Main(string[] args)
        {
            PrintMultiMessage("Katze", 1000);
            PrintMultiMessage("Mauzi", 1000);
            int age = 18;
            if (Checkage(age))
                Console.WriteLine("Du bist volljährig");
            else
                Console.WriteLine("Du bist minderjährig");


        }


        static void PrintMultiMessage(string message, int count)
        {
            while (count > 0)
            {
                Console.WriteLine(message);
                count-= 1;
            }
        }


        static bool Checkage(int age)
        {
            return age >= 18;




        }




    }

    















}
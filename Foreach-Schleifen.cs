using System;

namespace Objektorientierung
{
    class program
    {
        static void Main(string[] args)
        {
            Person Leon = new Person();
            Leon.Vorname = "Leon";
            Leon.Nachname = "Marzoll";
            Leon.SageEtwas(": Moin was geht !");

            Person Alex = new Person();
            Alex.Vorname = "Alex";
            Alex.Nachname = "Marzoll";
            Alex.SageEtwas(": Nicht viel und bei dir ?");

        }
    }
        class Person
        {
            public string Vorname { get; set; }
            public string Nachname { get; set; }
            public int Alter { get; set; }           
            //public Person(string vorname, string nachname, int Alter//
            
            public void SageEtwas(string satz)
            {
                Console.WriteLine(Vorname + " " + Nachname + " " + satz);

            }

        }
    







}





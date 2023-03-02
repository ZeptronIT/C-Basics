using System;

namespace Eigentschaften
{
    class Program
    {
        static void Main(string[] args)
        {
            Mauzi Lili = new Mauzi();
            Lili.Geburtsort = "Amerika";
            Lili.Rasse = "Maine-Coon";
            Lili.Pfoten = 4;
            Console.WriteLine(Lili.Geburtsort);
            Console.WriteLine(Lili.Rasse);
            Console.WriteLine(Lili.Pfoten);




        }


    }
    class Mauzi
    {
        public string Geburtsort { get; set; } // "private" muss in der gleichen Klasse verwendet werden//

        public string Rasse { get; set; }

        private int pfoten;
        public int Pfoten
        {
            get
            {
                return pfoten;
            }
            set
            {
                
                pfoten = value;
            }
        }
    }


}
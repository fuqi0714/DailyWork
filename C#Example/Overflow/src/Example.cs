using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _003Loop.src
{
    internal class Example
    {
        public static void Main(string[] args) {
            Example e = new Example();
            e.LoopTwo(int.Parse(args[0]));
            //e.Infinite();
        }
        public void Infinite() {
            Console.WriteLine("Infinite loop");
            Infinite();
        }
        public void LoopOne() {
            int sum = 1;
            for (int i = 1/*初始化表达式*/; i <= 5/*循环条件表达式*/; i++/*循环后的操作表达式*/) {
                sum *= i;
            }
            Console.WriteLine(sum);
        }
        public int LoopTwo(int getNum) {
            int start=getNum;
            for (; getNum > 2; getNum--)
            {
                start = start * (getNum-1);
                Console.WriteLine(start);
            }
            Console.WriteLine("----------------");
            
            return start;
        }
    }
}

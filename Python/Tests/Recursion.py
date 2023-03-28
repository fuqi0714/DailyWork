import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--times', type=str,required=True)
args = parser.parse_args()

'''
递归算法(英语: recursion algorithm)在计算机科学中是指一种通过重复将问题分解为同类的子问题而解决问题的方法。
递归式方法可以被用于解决很多的计算机科学问题，因此它是计算机科学中十分重要的一个概念。绝大多数编程语言支持函数的
自调用，在这些语言中函数可以通过调用自身来进行递归。计算理论可以证明递归的作用可以完全取代循环,因此在很多函数编
程语言中习惯用递归来实现循环
'''
class Recursion:
    def RecursionFun(self, times):
        value = times
        if times < 2:
            return value
        else:
            value = value * self.RecursionFun(times - 1)

            return value


if __name__ == '__main__':
    R = Recursion()
    print(R.RecursionFun(args.times))

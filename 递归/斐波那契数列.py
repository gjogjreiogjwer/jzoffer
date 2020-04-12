# -*- coding:utf-8 -*-
'''
裴波那契数列
写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项。斐波那契数列的定义如下：

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.

斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

解：使用简单的迭代。
'''

class Solution(object):
    # 递归，很慢，很多重复节点计算
    def fib1(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n
        return (self.fib(n-1) + self.fib(n-2)) % (1000000007)

    def fib(self, n):
        if n <= 1:
            return n
        first = 0
        second = 1
        for i in range(2, n+1):
            third = first + second
            first = second
            second = third
        return third % (1000000007)


if __name__ == '__main__':
    a = Solution()
    print (a.fib(4))

if __name__ == '__main__':
	b = Solution()
	print (b.Fibonacci(3))
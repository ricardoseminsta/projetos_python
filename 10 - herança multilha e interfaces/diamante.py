class A:
    def m1(self):
        print('método de A')


class B(A):
    def m2(self):
        print('metodo de B')


class C(A):
    def m2(self):
        print('metodo de C')


class D(B, C):
    pass


if __name__ == '__main__':

    d = D()
    d.m2()
    print(D.mro())
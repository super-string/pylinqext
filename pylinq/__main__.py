from pylinq import *


if __name__ == '__main__':
    from .cli import main
    main()
    
def main():
        
    # 数宇と文字が混ざったリスト
    p1 = pylist([1,"2",3,4,5,6,"7",8,9,10])
    print(p1)

    # selectというよりはOfType
    p2 = p1.select(lambda x : int(x))
    print(p2)

    # Method Chain
    p3 = p1.select(lambda x : int(x))\
            .where(lambda x : x % 2 == 0)
    print(p3)

    # Sum
    print(p2.sum())
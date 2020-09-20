from scheme import scheme
from week import week

if __name__ == '__main__':
    s = scheme("hej", 0, 0, 23, 59)
    print(s)
    print(s.check())
    w = week()
    w.addmonday(s)
    print(w)

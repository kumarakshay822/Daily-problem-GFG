class Students:
    def __init__(self,name, roll, dept, addr):
        self.name= name
        self.roll= roll
        self.dept= dept
        self.addr= addr
        def __str__(self):
            return f"{self.name} ({self.roll}){self.dept} {self.addr}"
        s1 = Students("John", 1, "IT", "BWN")
        print(s1)
        s2 = Students("Andrew", 2, "IT", "KOL")
        print(s2)
        s3 = Students("MIch", 3, "IT", "PAT")
        print(s3)
        s4 = Students("Michael", 4, "IT", "PAT")
        print(s4)
        s5 = Students("Teresa", 5, "IT", "AUBR")
        print(s5)
        s6 = Students("vivek", 6, "IT", "PES")
        print(s6)
        s7 = Students("Vikash", 7, "IT", "GAYA")
        print(s7)
        s8 = Students("Ambuj", 8, "IT", "CHENN")
        print(s8)
        s9 = Students("Sanjay", 9, "IT", "COIM")
        print(s9)
        s10 = Students("Vickey", 10, "IT", "NAB")
        print(s10)
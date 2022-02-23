class Grandfather:
    def __init__(self):
        self.myname = 'GrandFather'
        self.father = self.Father()
            
    def mydisplay(self):
        print("Good Morning!", self.myname)
        self.father.myfather()
        self.father.son.Iamson()
    
    class Father:
        def __init__(self):
            self.son = self.Son()
        def myfather(self):
            print("Good Morning! Father")
        
        class Son:
            def Iamson(self):
                print("Good Morning! Son")

myobj = Grandfather()
myobj.mydisplay()
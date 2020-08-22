intro="""
          
   ____      _       ____        _       ____  U _____ u       ____      _      _   _    ____    
U /"___|uU  /"\  uU |  _"\ u U  /"\  uU /"___|u\| ___"|/    U | __")uU  /"\  u | \ |"|  |  _"\   
\| |  _ / \/ _ \/  \| |_) |/  \/ _ \/ \| |  _ / |  _|"       \|  _ \/ \/ _ \/ <|  \| |>/| | | |  
 | |_| |  / ___ \   |  _ <    / ___ \  | |_| |  | |___        | |_) | / ___ \ U| |\  |uU| |_| |\ 
  \____| /_/   \_\  |_| \_\  /_/   \_\  \____|  |_____|       |____/ /_/   \_\ |_| \_|  |____/ u 
  _)(|_   \\    >>  //   \\_  \\    >>  _)(|_   <<   >>      _|| \\_  \\    >> ||   \\,-.|||_    
 (__)__) (__)  (__)(__)  (__)(__)  (__)(__)__) (__) (__)    (__) (__)(__)  (__)(_")  (_/(__)_)   

"""


#----------------------------------------------
from abc import abstractmethod,ABC
from itertools import product

class Band :
    '''
    This class brings all the members together to make a band
    '''
    to_list = []
    def __init__(self, name, members):
        self.name = name
        self.members = list(members)###
        Band.to_list.append(self)
    
    def play_solos(self):
        # return [person + 'play solo' for person in self.members]
        play=['play a solos']
        return(list(product(self.members,play)))


   #@property
    def __str__(self):
        return f'Band Data => ( Name : {self.name} , Members: {self.members})'

    #@property
    def __repr__(self):
        return f'Band Data => (Name : {self.name} , Members: {self.members})'


#----------------------------------------------
class Musician(ABC):
    '''
    This class contains the common atrr an methods ,so we can use them
     in(Guitarist,Bassist,Drummer) clases
    '''
    def __init__(self, name):
     self.name = name

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def get_instrument(self):
        pass

    @abstractmethod
    def play_solo(self):
        pass

#----------------------------------------------

class Guitarist(Musician):
    '''
    This class to create a Guitarist member
    '''
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"The name:{self.name}"
    def __repr__(self):
        return f"Guitarist : {self.name}"
    def get_instrument(self):
        return "instrument : Guitar"
    def play_solo(self):
        return "play_solo from Guitarist class"
#----------------------------------------------

class Bassist(Musician):
    '''
    This class to create a Musician member
    '''
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"The name:{self.name}"
    def __repr__(self):
        return f"Bassist : {self.name}"
    def get_instrument(self):
        return "instrument : Bass"
    def play_solo(self):
        return "play_solo from Bassist class"
#----------------------------------------------
 
class Drummer(Musician):
    '''
    This class to create a Drummer member
    '''
    def __init__(self, name):
        super().__init__(name)

    def __str__(self):
        return f"The name:{self.name}"
    def __repr__(self):
        return f"Drummer : {self.name}"
    def get_instrument(self):
        return "instrument : drums"
    def play_solo(self):
        return "play_solo from Drummer class"
#----------------------------------------------


if __name__ == "__main__":
    print(intro)
    Alan_Waker = Guitarist('Alan Waker')
    print(Alan_Waker.name)
    print("*"*50)
    print(Alan_Waker)
    print("*"*50)
    print(Alan_Waker.get_instrument())
    print("*"*50)
    print(Alan_Waker.play_solo())
    print("*"*50)
    # _________________________________________
    sia = Bassist('sia')
    Dan_Reynolds=Drummer('Dan Reynolds')
    Imagine_Dragons_test= (Band("Imagine Dragons", [Alan_Waker,sia,Dan_Reynolds]))
    print(Imagine_Dragons_test.name)
    print(Imagine_Dragons_test.members)
    print(Imagine_Dragons_test.play_solos())
    print("*"*50)
    # print(Imagine_Dragons_test.to_list)
    # _________________________________________
    kygo=Bassist('kygo')
    marshmello=Drummer('marshmello')
    Imagine_Dragons_test= (Band("OK Go band", [kygo,marshmello]))
    print(Band.to_list)
    print("*"*50)



        # repl.it
        # from itertools import product
        # let=['play a solos']
        # listt=['dana','mais','hala']
        # x=list(product(let,listt))
        # print(list(product(listt,let)))






















    

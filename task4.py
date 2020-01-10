class ContacList(list):
    def __init__(self,*args):
        self.novyi_list = []
        for x in args:
            self.novyi_list.append(x)

    def search_by_name(self,name):
        for x in self.novyi_list:
            if x == name:
                print(f'{x}')
            else:
                pass


all_contacts = ContacList('Adilet','Ryspek','Sanjar','Alina','Adilet')

all_contacts.search_by_name('Adilet')





    


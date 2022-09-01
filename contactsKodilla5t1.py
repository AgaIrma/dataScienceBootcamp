from faker import Faker

class BaseContact:

    def __init__(self, firstName, lastName, email, phone):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.phone = phone

    def __len__(self):
        length = len(self.firstName) + len(self.lastName)
        print(length)
        
    def __str__(self):
        return f'{self.firstName} {self.lastName} {self.email} {self.phone}'

    def contact(self):
        print(" Wybieram numer ",self.phone ," i dzwonie do ", self.firstName, " ", self.lastName)


class BusinessContact(BaseContact):

    def __init__(self, job, company, businessPhone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.job = job
        self.company = company
        self.businessPhone = businessPhone

    def __str__(self):
        return f'{self.firstName} {self.lastName} {self.email} {self.phone} {self.job} {self.company}  '   

    def contact(self):
         print(" Wybieram numer ",self.businessPhone ," i dzwonie do ", self.firstName, " ", self.lastName)

def createContacts(typeOfObject, amount):
    if typeOfObject == 1:
        for i in range (amount):
            print(BaseContact(fakeobject.first_name(),fakeobject.last_name(), fakeobject.first_name()[:1]+fakeobject.last_name()+'@gmail.com', fakeobject.phone_number() ))
    if typeOfObject == 2:
        for i in range (amount):
            print(BusinessContact(fakeobject.job(),fakeobject.company(), fakeobject.phone_number(), fakeobject.first_name(),fakeobject.last_name(), fakeobject.email(),fakeobject.phone_number()))
            
    
jan = BaseContact('an','Kowalski', 'jkowalski@gmail.com','999-999-999')
jan.contact()
jan.__len__()

janBusinesowy = BusinessContact('Mechanik', 'Smyk','111-111-111','an','Kowalski', 'jkowalski@gmail.com','999-999-999' )
janBusinesowy.contact()
janBusinesowy.__len__()

fakeobject = Faker()
createContacts(1,2)
createContacts(2,2)
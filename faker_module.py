import pandas as pd
from faker import Faker
import random
fake = Faker('en_IN')

class DataGenerator:
    def __init__(self, n):
        self.n = n

    def names(self):
        return [fake.name() for i in range (self.n)]
    
    def address(self):
        return [fake.address() for i in range (self.n)]
    
    def postcode(self):
        return [int(fake.postcode()) for i in range (self.n)]
    
    def age(self):
        return [random.randint(21,66) for i in range(self.n)]
    
    def lang(self):
        india_languages = ['Hindi', 'Bengali', 'Telugu', 'Marathi',
                   'Tamil', 'Gujarati', 'Urdu', 'Kannada', 'Odia',
                   'Punjabi', 'Malayalam', 'Assamese']
        return [random.choice(india_languages) for i  in range (self.n)]
    
    def mobile_numbers(self):
        mobile_no = []
        l = 0
        while l<self.n:
            fnum = fake.phone_number()
            if len(fnum) == 10 and fnum.startswith(random.choice(['7','8','9'])):
                mobile_no.append(int(fnum))
                l += 1
        return mobile_no
    
    def aadhaar(self):
        return [int(fake.aadhaar_id()) for i in range (self.n)]
    
    def email(self):
        email_domains = ['gmail.com', 'yahoo.com', 'hotmail.com',
                 'outlook.com', 'aol.com', 'protonmail.com',
                 'icloud.com', 'zoho.com','rediffmail.com']
        return [fake.email().split('@')[0] + '@'+random.choice(email_domains)
               for i in range(self.n)]
    
    def job(self):
        return [fake.job() for i in range (self.n)]
    
    def esal(self):
        return [random.randint(10000,50000) for i in range(self.n)] 
    
    def bank(self):
        return [fake.bank() for i in range (self.n)]
    
    def bankac(self):
        return [fake.bban() for i in range (self.n)]
    



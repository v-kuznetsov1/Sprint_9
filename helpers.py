
from faker import Faker

class GenerateUserData:
    
    faker = Faker()

    first_name = faker.first_name()
    last_name = faker.last_name()
    user_name = faker.user_name()
    email = faker.email()
    password = faker.password(length=8, digits=True)

    
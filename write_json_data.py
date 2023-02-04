from faker import Faker
import json

def write_json():
    fake = Faker()
    fakedata = []
    
    for detail in range(1000):
        details = {"name":fake.name(),
                    "age":fake.random_int(min=20, max=65, step=1),
                    "city":fake.city()}

        fakedata.append(details)

        with open("data.json", "w", newline='') as f:
            json.dump(fakedata, f)

write_json()
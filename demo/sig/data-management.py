import csv
import re
import zipcodes
from names_dataset import NameDataset

nd = NameDataset()
debug = False

def validate_first_name(test):
    if test.isalpha():
        return True
    else:
        return False

def validate_last_name(test):
    if test.isalpha():
        return True
    else:
        return False

def validate_ip_address(test):
    invalid_starts = ['0', '127', '169', '172', '192']
    # print (f'Testing {test}')
    if test.count(".") != 3:
        return False
    elif ':' in test:
        return False
    elif test.split(".")[0] in invalid_starts:
        return False
    if (
        (test.count(".") == 3 and int(test.split(".")[0]) <= 255 and int(test.split(".")[1]) <= 255 and int(test.split(".")[2]) <= 255 and int(test.split(".")[3]) <= 255)
        ) :
        return True
    else:
        return False

def validate_email_address(test):
    if '@gmial.com'  in test:
        return False
    elif '@guerillamail.com' in test:
        return False
    elif "@" in test and "." in test:
        return True
    else:
        return False

def validate_address(test):
    
    # Find zip codes inside of test - 5 digits
    zip = re.findall(r'\b\d{5}\b', test)
    if zip != [] and zipcodes.is_real(zip[0]):
        # [{'zip_code': '83702', 'zip_code_type': 'STANDARD', 'active': True, 'city': 'Boise', 
        # 'acceptable_cities': [], 'unacceptable_cities': [], 'state': 'ID', 'county': 'Ada County',
        # 'timezone': 'America/Boise', 'area_codes': ['208'], 'world_region': 'NA', 'country': 'US', 'lat': '43.6645', 'long': '-116.1646'}][city]
        city = zipcodes.matching(zip[0])[0]['city']
        if not city in test:
            print (f'\tCity {city} NOT FOUND!')
        else:
            # print (f'\tFound zip code {zip[0]} for {city}')
            pass
        
    if test == "null":
        return False
    elif test == "":
        return False
    elif test.count(",") == 0:
        return False
    elif " or " in test:
        return False
    elif "1600 Amphitheatre Parkway Mountain View, CA 94043" in test:
        return False
    elif zip == []:
        return False
    if test.count(" ") >= 2:
        return True
    else:
        return False

# Read in the data file "data-in.csv" into a CSV structure.  The first row has the header names
# and the subsequent rows have the data.
data = []
with open('data-in.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data.append(row)

# Print the names of the headers to be sure
print(data[0].keys())

def validate_name(first_name, last_name):
    name_result = nd.search(first_name)
    # print (name_result)
    # Add up the scores for each name in the first_name : rank dictionary
    first_as_first = 0
    for rank in name_result['first_name']['rank']:
        result = name_result['first_name']['rank'][rank]
        if result != 'None' and result != None:
            first_as_first = first_as_first + int(result)
            
    # Similarly for the last name
    first_as_last = 0
    for rank in name_result['last_name']['rank']:
        result = name_result['last_name']['rank'][rank]
        if result != 'None' and result != None:
            first_as_last = first_as_last + int(result)
    
    # do the same for the last_name
    name_result = nd.search(last_name)
    # print (name_result)
    last_as_first = 0
    try:
        for rank in name_result['first_name']['rank']:
            result = name_result['first_name']['rank'][rank]
            if result != 'None' and result != None:
                last_as_first = last_as_first + int(result)
    except TypeError:
        pass

    last_as_last = 0
    try:
        for rank in name_result['last_name']['rank']:
            result = name_result['last_name']['rank'][rank]
            if result != 'None' and result != None:
                last_as_last = last_as_last + int(result)
    except TypeError:
        pass

    # print (f'The name {first_name} {last_name} is ranked as ({first_as_first},{first_as_last}) and ({last_as_first}, {last_as_last})')

    if first_as_first < last_as_first and last_as_last < first_as_last:    
        if debug: print (f'\tThe name {first_name} {last_name} is likely correct')
    elif last_as_first < first_as_first and first_as_last < last_as_last:
        print (f'\tThe name {first_name} {last_name} may be backwards')
    else:
        print (f'\tThe name {first_name} {last_name} is has ambiguous ordering')

# Now let's iterate through the data and validate each entry
for row in data:
    first_name = row["First Name"]
    last_name = row["Last Name"]
    ip_address = row["IP Address"]
    email_address = row["Email Address"]
    delivery_address = row["Delivery Address"]
    
    print(f'Testing {first_name}, {last_name}, {ip_address}, {email_address}, {delivery_address}')
    validate_name(first_name, last_name)
    ip_address_valid = validate_ip_address(ip_address)
    if ip_address_valid:
        if debug: print(f'\tThe IP address [{ip_address}] is valid')
    else:
        print(f'\tThe IP address [{ip_address}] is not valid')
    email_address_valid = validate_email_address(email_address)
    if email_address_valid:
        if debug: print(f'\tThe email address [{email_address}] is valid')
    else:
        print(f'\tThe email address [{email_address}] is not valid')
    delivery_address_valid = validate_address(delivery_address)
    if delivery_address_valid:
        if debug: print(f'\tThe delivery address [{delivery_address}] is valid')
    else:
        print(f'\tThe delivery address [{delivery_address}] may not be valid')
    
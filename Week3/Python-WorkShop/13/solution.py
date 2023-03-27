import re

def main(names):
    
    name_list = names.split(',')

    
    email_count = {}

    
    output = []

    for name in name_list:
        
        name = name.strip()

        
        first_name, last_name = name.split(' ')[0], name.split(' ')[-1]

        
        first_name = re.sub('[^a-zA-Z]', '', first_name)
        last_name = re.sub('[^a-zA-Z]', '', last_name)

        
        base_email = f"{first_name}.{last_name}@company.com".lower()

        
        if base_email not in email_count:
            email_count[base_email] = 1
            output.append((name, base_email))
        else:
            email_count[base_email] += 1
            new_email = f"{first_name}.{last_name}{email_count[base_email]}@company.com".lower()
            output.append((name, new_email))

    return output
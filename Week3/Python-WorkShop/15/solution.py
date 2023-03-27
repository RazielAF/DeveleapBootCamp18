def main(s):
   modified_str = ''
   for index, char in enumerate(s):
        modified_str += char.upper() + char.lower() * index + '-'
   return modified_str[:-1]
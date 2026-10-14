# FUNCTIONS TO PARSE DATA

def parse_headers(header_line):
   return header_line.strip().split(',')
_____________________________________________________________________________________________________________________________

def parse_values(data_line):
  values=[]
  for item in data_line.strip().split(','):
    if(item==''):
       values.append(0.0)
    else :
       values.append(float(item))
  return values

_____________________________________________________________________________________________________________________________


def create_dict(values, headers):
  result={}
  for value,header in zip(values,headers):
    result[header]=value
  return result

_____________________________________________________________________________________________________________________________

#Final Read CSV function 

def read_csv(path) :
  result=[]

  with open(path, 'r') as f:
    lines=f.readlines()

  headers=parse_headers(lines[0])

  for data_line in lines[1:]:
    values=parse_values(data_line)

    item_dict=create_dict(values, headers)
    result.append(item_dict)

  return result

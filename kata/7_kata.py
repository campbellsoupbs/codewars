def solution(n):
  units = {0:"", 1:"I", 2:"II", 3:"III", 4:"IV", 5:"V", 6:"VI", 7:"VII", 8:"VIII", 9:"IX"}
  tens = {0:"", 1:"X", 2:"XX", 3:"XXX", 4:"XL", 5:"L", 6:"LX", 7:"LXX", 8:"LXXX", 9:"XC"}
  hund = {0:"", 1:"C", 2:"CC", 3:"CCC", 4:"CD", 5:"D", 6:"DC", 7:"DCC", 8:"DCCC", 9:"CM"}
  thousand = {0:"", 1:"M", 2:"MM", 3:"MMM"}

  sn = str(n)

  try:
    n_units = int(sn[-1])
    roman_units = units[n_units]
  except:
    roman_units = ""

  try:
    n_tens = int(sn[-2])
    roman_tens = tens[n_tens]
  except:
    roman_tens = ""

  try:
    n_hund = int(sn[-3])
    roman_hund = hund[n_hund]
  except:
    roman_hund = ""

  try:
    n_tho = int(sn[-4])
    roman_tho = thousand[n_tho]
  except:
    roman_tho = ""


  return f'{roman_tho}{roman_hund}{roman_tens}{roman_units}'

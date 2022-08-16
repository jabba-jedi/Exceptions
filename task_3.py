#!/usr/bin/env python3

import re

class MyCripto:
  def __init__(self, shift: int):
    if shift > 26 or shift < -26:
      shift = shift % 26
    self.shift = shift


  def encrypt(self, my_string):
    '''Encrypts the given string by shifting all letters in it
    to the given position. Returns a string'''
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    isUpcase = False

    my_list = list(my_string)
    my_string_encoded = []
    for l in my_list:
      try:
        if l.lower() in alphabet:
          if l != l.lower():
            isUpcase = True
          new_index = alphabet.index(l.lower()) + self.shift
          if new_index > len(alphabet) - 1:
            new_index =  new_index - 26
          new_symbol = alphabet[new_index]
          if isUpcase:
            my_string_encoded.append(new_symbol.upper())
            isUpcase = False
          else:
            my_string_encoded.append(new_symbol)
        else:
          raise ValueError('Only English symbols accepted')
      except ValueError as e:
        print('Only English symbols accepted')
        break
    if my_string_encoded != []:
      return ''.join(my_string_encoded)
    else:
      return my_string

  def decrypt(self, my_string):
    '''Decrypts the given string by shifting all letters in it
    to the given position. Returns a string'''
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    isUpcase = False

    my_list = list(my_string)
    my_string_decoded = []
    for l in my_list:
      try:
        if l.lower() in alphabet:
          if l != l.lower():
            isUpcase = True
          new_index = alphabet.index(l.lower()) - self.shift
          if new_index > len(alphabet) - 1:
            new_index =  new_index - 26
          new_symbol = alphabet[new_index]
          if isUpcase:
            my_string_decoded.append(new_symbol.upper())
            isUpcase = False
          else:
            my_string_decoded.append(new_symbol)
        else:
          raise ValueError('Only English symbols accepted')
      except ValueError as e:
        print('Only English symbols accepted')
        break
    if my_string_decoded != []:
      return ''.join(my_string_decoded)
    else:
      return my_string

# testcases
#shifts = [0, 3, 33, 145, -7, -40]
#for shift in shifts:
#  my_test = MyCripto(shift)
#  print("Shift: " , shift)
#  print(my_test.encrypt("cat"))
#  print(my_test.decrypt("fdw"))
#  print(my_test.encrypt("кот"))
#  print(my_test.encrypt("Axolotl"))
#  print(my_test.decrypt("Darorwo"))

# main logic
welcome_string = "Welcome to MyCripto. Options:\n- \
  provide an integer to serve as a basis for encoding/decoding\n \
  - enter `encrypt ` followed by your string to encode it\n \
  - enter `decrypt ` followed by your string to decode it\n \
  - enter `exit` to stop the app"


user_input = input(welcome_string).strip()

while user_input != 'exit':
  if 'encrypt' in user_input:
    m = re.search(r'^(encrypt) (.+)$', user_input)
    my_word = m.group(2)
    if shift:
      print(MyCripto(shift).encrypt(my_word))
      user_input = input(welcome_string)
    else:
      user_input = input(welcome_string)
  elif 'decrypt' in user_input:
    m = re.search(r'^(decrypt) (.+)$', user_input)
    my_word = m.group(2)
    if shift:
      print(MyCripto(shift).decrypt(my_word))
      user_input = input(welcome_string)
    else:
      user_input = input(welcome_string)
  elif int(user_input):
    shift = int(user_input)
    print("Successfully set the shift key: ", shift)
    user_input = input(welcome_string)
  else:
    user_input = input(welcome_string)

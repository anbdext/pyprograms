def parse_encoded_string(encoded_string):
 

  values = encoded_string.split("0")
  values = [value for value in values if value]

  parsed_string = {
      "first_name": values[0],
      "last_name": values[1],
      "id": values[2]
  }

  return parsed_string

encoded_string = "Arjun0000000Ram0001247473"
parsed_string = parse_encoded_string(encoded_string)

print(parsed_string)

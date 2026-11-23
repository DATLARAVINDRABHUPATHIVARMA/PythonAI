Conversions = {
    5:"Jemimah Rodrigues",
    31:"Shreyanka Patil",
    18:"Smriti Mandhana",
    "AC":"Alice Capsey",
    "SE":"Sophie Ecclestone",
    "RG":"Richa Ghosh",
    "GV":"Georgia Voll",
    "AK":"Alana King",
    "AG":"Ashleigh Gardner",
    "NSB":"Nat-Sciver Brunt",
    "EP":"Ellyse Perry"
}

print(Conversions["AC"]) # Printing the value based on the key
print(Conversions[5]) # Printing the value based on the key

# get function for printing value
print(Conversions.get("AK"))

# Invalid Case with get
print(Conversions.get("RR", "Invalid Key"))
marks = {
    "Saurabh": 100,
    "Shubham": 56,
    "Rohan": 23,
    0: "Saurabh"
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Saurabh": 99, "Renuka": 100})
# print(marks)

print(marks.get("Saurabh2")) # Prints None
print(marks["Saurabh2"]) # Returns an error
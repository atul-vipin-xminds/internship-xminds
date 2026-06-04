def get_names(pages):
    for page in pages:
        for name in page:
            yield name

pages = [
    ["Rahul", "Anu"],
    ["John", "Priya"],
    ["Arun", "Meera"]
]

for name in get_names(pages):
    print(name)
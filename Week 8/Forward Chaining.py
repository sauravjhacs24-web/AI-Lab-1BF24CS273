


facts = [
    ("Parent", "john", "mary"),
    ("Parent", "mary", "susan"),
    ("Parent", "john", "peter"),
    ("Parent", "peter", "alice")
]



def forward_chaining(facts):
    new_facts = True

    while new_facts:
        new_facts = False

        parents = [
            (x, y) for relation, x, y in facts
            if relation == "Parent"
        ]

        for x, y in parents:
            for y2, z in parents:
                if y == y2:
                    new_fact = ("Grandparent", x, z)

                    if new_fact not in facts:
                        facts.append(new_fact)
                        print("New Fact Generated:", new_fact)
                        new_facts = True

    return facts



print("Initial Knowledge Base:")
for fact in facts:
    print(fact)


print("\nApplying Forward Chaining...")
facts = forward_chaining(facts)


query = ("Grandparent", "john", "susan")

print("\nQuery:", query)

if query in facts:
    print("Query Proved Successfully!")
else:
    print("Query Cannot Be Proved.")
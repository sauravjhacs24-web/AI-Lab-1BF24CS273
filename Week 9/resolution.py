clauses = [
    {"Parent(John,Mary)"},
    {"Parent(Mary,Susan)"},
    {"NOT Parent(John,Mary)",
     "NOT Parent(Mary,Susan)",
     "Grandparent(John,Susan)"}
]

# Negated Query
query = "Grandparent(John,Susan)"
negated_query = "NOT " + query

clauses.append({negated_query})


# Resolution Function
def resolve(c1, c2):
    resolvents = []

    for literal in c1:
        if literal.startswith("NOT "):
            complement = literal[4:]
        else:
            complement = "NOT " + literal

        if complement in c2:
            new_clause = (c1 - {literal}) | (c2 - {complement})
            resolvents.append(new_clause)

    return resolvents


# Resolution Algorithm
def resolution(clauses):
    new = set()

    while True:
        pairs = [
            (clauses[i], clauses[j])
            for i in range(len(clauses))
            for j in range(i + 1, len(clauses))
        ]

        for c1, c2 in pairs:
            resolvents = resolve(c1, c2)

            for resolvent in resolvents:

                # Empty clause means contradiction
                if len(resolvent) == 0:
                    print("Empty Clause Generated: {}")
                    return True

                new.add(frozenset(resolvent))

        if new.issubset(set(map(frozenset, clauses))):
            return False

        for clause in new:
            if clause not in set(map(frozenset, clauses)):
                clauses.append(set(clause))


# Display Knowledge Base
print("Knowledge Base:")
for clause in clauses:
    print(clause)

# Prove Query
print("\nQuery:", query)
print("Adding Negated Query:", negated_query)

print("\nApplying Resolution...")

if resolution(clauses):
    print("Contradiction Found!")
    print("Query Proved Successfully!")
else:
    print("Query Cannot Be Proved.")
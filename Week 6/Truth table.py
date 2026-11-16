from itertools import product


def KB(P, Q):
    # KB: P AND (P implies Q)
    return P and ((not P) or Q)


def query(P, Q):
   
    return Q


def truth_table_entails():
    symbols = ['P', 'Q']
    entails = True

    print("P\tQ\tKB\tQuery")

    for values in product([True, False], repeat=2):
        P, Q = values

        kb_value = KB(P, Q)
        query_value = query(P, Q)

        print(f"{P}\t{Q}\t{kb_value}\t{query_value}")

        if kb_value and not query_value:
            entails = False

    if entails:
        print("\nKB entails the Query.")
    else:
        print("\nKB does not entail the Query.")


truth_table_entails()
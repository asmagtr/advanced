ppl = int(input("How many people need a ride? "))
cpct = int(input("How many people fit in one taxi? "))

taxis= ppl // cpct
rest = ppl % cpct

if rest > 0:
    taxis=taxis + 1

print(f"Number of taxis needed: {taxis}")
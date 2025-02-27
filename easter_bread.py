budget = float(input())
one_kg_flour_price = float(input())

one_pack_eggs_price = one_kg_flour_price * 0.75
one_l_milk_price = one_kg_flour_price * 1.25
needed_funds_for_one_loaf = one_pack_eggs_price + one_kg_flour_price + (one_l_milk_price * 0.25)

colored_eggs = 0
loaves = 0

while True:
    if budget < needed_funds_for_one_loaf:
        break

    loaves += 1
    colored_eggs += 3
    budget -= needed_funds_for_one_loaf

    if loaves % 3 == 0:
        colored_eggs -= (loaves - 2)

print(f"You made {loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")


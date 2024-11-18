"""Examples of dictionary syntax with Ice Cream Shop Order tallies."""

ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}

# len evaluated to number of key-value entries
print(len(ice_cream))

# Add key-value entries using suvrcrition notation
ice_cream["mint"] = 10

# Access values by their key using subscription
mint_orders: int = ice_cream["mint"]
print(mint_orders)

# Re-assign values by their key using assignment
ice_cream["mint"] = ice_cream["mint"] + 1
# or
ice_cream["mint"] += 1

# Remove items by key using the pop method
ice_cream.pop("strawberry")

# Test if a key is in the dictionary:
print("vanilla" in ice_cream)
# Loop through items using for-in loops
# total: int = 0
# The variable (e.g. flavor) iterates over
# each key one-by-one in the dictonary
for flavor in ice_cream:
    tally: int = ice_cream[flavor]
    print(f"{flavor}: {tally}")

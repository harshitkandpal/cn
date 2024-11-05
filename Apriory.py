from itertools import combinations
# Sample dataset
data = [
    ['A', 'B', 'C'],
    ['A', 'C'],
    ['A', 'D'],
    ['B', 'C'],
    ['A', 'C', 'D'],
    ['B', 'C', 'E']
]

# Set minimum support and confidence
min_sup = 2
min_conf = 0.6

# Generate frequent itemsets
def apriori(data, min_sup):
    freq_items = {}
    item_count = {}
    k = 1

    # Generate initial 1-itemsets
    for row in data:
        for item in row:
            if (item,) not in item_count:
                item_count[(item,)] = 0
            item_count[(item,)] += 1
    
    # Filter by min_sup
    freq_items[k] = {k: v for k, v in item_count.items() if v >= min_sup}
    
    # Generate larger itemsets
    while len(freq_items[k]) > 0:
        k += 1
        item_count = {}

        # Combine pairs of frequent itemsets from previous level
        prev_items = list(freq_items[k-1].keys())
        for i in range(len(prev_items)):
            for j in range(i+1, len(prev_items)):
                itemset = tuple(sorted(set(prev_items[i]) | set(prev_items[j])))
                if len(itemset) == k:
                    # Count occurrences
                    if itemset not in item_count:
                        item_count[itemset] = 0
                    for row in data:
                        if all(item in row for item in itemset):
                            item_count[itemset] += 1

        # Filter by min_sup
        freq_items[k] = {k: v for k, v in item_count.items() if v >= min_sup}
    
    # Collect all frequent itemsets
    all_freq_items = {}
    for k, items in freq_items.items():
        all_freq_items.update(items)
    
    return all_freq_items

# Generate association rules
def assoc_rules(freq_items, min_conf):
    rules = []
    for itemset in freq_items:
        if len(itemset) < 2:
            continue
        sup_count = freq_items[itemset]
        for i in range(1, len(itemset)):
            for left in combinations(itemset, i):
                right = tuple(sorted(set(itemset) - set(left)))
                conf = sup_count / freq_items[left]
                if conf >= min_conf:
                    rules.append((left, right, conf))
    return rules

# Run Apriori and print results
freq_items = apriori(data, min_sup)
rules = assoc_rules(freq_items, min_conf)

print("Frequent Itemsets:")
for itemset, count in freq_items.items():
    print(f"{itemset}: {count}")

print("\nAssociation Rules:")
for left, right, conf in rules:
    print(f"{left} => {right} (conf: {conf:.2f})")
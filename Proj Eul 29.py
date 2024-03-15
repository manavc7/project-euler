results = [a**b for a in range(2,101) for b in range(2,101)]
distinct_results = []
for i in results:
    if i not in distinct_results:
        distinct_results.append(i)

print(len(distinct_results))
print(len(set(results)))

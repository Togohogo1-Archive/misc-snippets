from random import randint

lo = 1
hi = 10

loop = 1000000

freq_b = {i: 0 for i in range(lo, hi+1)}
freq_c = {i: 0 for i in range(lo, hi+1)}

error_margin_b = 0
error_margin_c = 0
error_diff = 5

# Python's builtin RNG
def builtin_rand(lo, hi):
    return randint(lo, hi)

# Custom RNG
def custom_rand(lo, hi):
    return randint(lo, hi)


# freq[i] = frequency of number within a range from hi to lo
for i in range(loop):
    freq_b[builtin_rand(lo, hi)] += 1
    freq_c[custom_rand(lo, hi)] += 1

# Apply percentage error formula for each number in range, and sum then all up
# Theoretical frequency of each number in range vs. Actual frequency of each number in range
for i in range(lo, hi+1):
    error_margin_b += abs(((loop/(hi-lo+1)-freq_b[i])/(loop/(hi-lo+1)))*100)
    error_margin_c += abs(((loop/(hi-lo+1)-freq_c[i])/(loop/(hi-lo+1)))*100)

# Take the average error margin
avg_emb = error_margin_b/(hi-lo+1)
avg_emc = error_margin_c/(hi-lo+1)

print(f"Builtin Average Error Margin: {avg_emb:.6f}")
print(f"Custom Average Error Margin: {avg_emc:.6f}")
print(f"Average Error Margin Difference: {abs(avg_emb - avg_emc):.6f}")

if abs(avg_emb - avg_emc) <= error_diff:
    print("AC")
else:
    print("WA")

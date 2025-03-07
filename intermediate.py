def TaskOfPairing(freq):
    pairs = 0
    leftover = 0
    
    for x in freq:
        # Pair leftover from previous weight with current weight
        cross = min(leftover, x)
        pairs += cross
        x -= cross
        leftover -= cross
        
        # Pair among themselves
        pairs += x // 2
        leftover = x % 2
    
    return pairs

# ---------------
# Example usage:
# freq = [4, 3, 5, 2] -> expected 7
print(TaskOfPairing([4, 3, 5, 2]))  # should print 7


def authEvents(events):
    MOD = 10**9 + 7
    P   = 131

    def hashString(s):
        h = 0
        for c in s:
            h = (h * P + ord(c)) % MOD
        return h

    # Current password's hash
    curHash = 0
    
    results = []
    for eType, param in events:
        if eType == "setPassword":
            # Re-hash the new password
            curHash = hashString(param)

        elif eType == "authorize":
            x = int(param)
            
            # 1) If x == hash(currentPassword)
            if x == curHash:
                results.append(1)
                continue
            
            # 2) If x == hash(currentPassword + c)
            #    => x == (curHash * P + ord(c)) mod MOD
            #    => ord(c) = (x - (curHash*P) + MOD) % MOD
            appended = (x - (curHash * P) % MOD + MOD) % MOD
            
            # Check if appended is the ASCII of [0–9A–Za–z]
            if (48 <= appended <= 57) or (65 <= appended <= 90) or (97 <= appended <= 122):
                results.append(1)
            else:
                results.append(0)

    return results



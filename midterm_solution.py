# Mobile Legends Match Tracker

# Get player info
ign = input("Enter your IGN: ")
rank = input("Enter your Rank (Epic, Legend, Mythic, etc.): ")

# Hero roster
heroes = ["Alucard", "Miya", "Tigreal", "Eudora", "Lancelot"]

print("\nHero Roster:")
for i in range(len(heroes)):
    print(f"{i+1}. {heroes[i]}")

# Storage for match data
matches = []

# Input for 4 matches
for match_num in range(1, 5):
    print(f"\nMatch {match_num}")
    hero_choice = int(input("Choose hero (1–5) or 0 to skip: "))

    if hero_choice == 0:
        print("Match skipped.")
        continue

    if 1 <= hero_choice <= 5:
        hero = heroes[hero_choice - 1]

        kills = int(input("Kills: "))
        deaths = int(input("Deaths: "))
        assists = int(input("Assists: "))
        result = input("Result (W/L): ").upper()

        # Avoid division by zero
        if deaths == 0:
            deaths = 1

        # Compute KDA
        kda = (kills + assists) / deaths

        # Determine performance tag
        if kda >= 5 and result == "W":
            tag = "DOMINATION!"
        elif kda >= 5 and result == "L":
            tag = "Carried Hard"
        elif kda < 5 and result == "W":
            tag = "Team Effort"
        else:
            tag = "Better Luck Next Game"

        # Store match info
        matches.append({
            "match": match_num,
            "hero": hero,
            "kda": kda,
            "result": result,
            "tag": tag
        })
    else:
        print("Invalid choice. Match skipped.")

# Calculate totals
wins = 0
losses = 0

for m in matches:
    if m["result"] == "W":
        wins += 1
    elif m["result"] == "L":
        losses += 1

total_games = wins + losses
win_rate = int((wins / total_games) * 100) if total_games > 0 else 0

# Find best match (highest KDA)
best_match = None
highest_kda = 0

for m in matches:
    if m["kda"] > highest_kda:
        highest_kda = m["kda"]
        best_match = m

# Display results
print("\n===== MATCH LOG =====")
print(f"Player: {ign}")
print(f"Rank: {rank}\n")

for m in matches:
    print(f"Match {m['match']}:")
    print(f" Hero: {m['hero']}")
    print(f" KDA: {m['kda']:.2f}")
    print(f" Result: {m['result']}")
    print(f" Tag: {m['tag']}\n")

print("===== SUMMARY =====")
print(f"Wins: {wins}")
print(f"Losses: {losses}")
print(f"Win Rate: {win_rate}%")

if best_match:
    print("\nBest Match:")
    print(f" Match {best_match['match']} with {best_match['hero']} (KDA: {best_match['kda']:.2f})")
else:
    print("\nNo matches recorded.")

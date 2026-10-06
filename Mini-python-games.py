import random, sys

def main():
    print("=" * 30 + "\n🏰 DUNGEON PULSE v1.0 🏰\n" + "=" * 30)
    name = input("Enter Hero Name: ") or "Ranger"
    hp, gold, stage = 120, 20, 1
    
    while True:
        print(f"\n📍 Stage {stage} | ❤️ HP: {hp} | 🪙 Gold: {gold}")
        act = input("Action: [1] Delve Dungeon [2] Camp (15g) [3] Quit -> ").strip()
        
        if act == "1":
            enemy = random.choice(["Slime", "Specter", "Dread Knight"])
            e_hp = random.randint(25, 55) + (stage * 5)
            e_atk = random.randint(6, 14) + stage
            print(f"⚠️ Ambushed by a {enemy} (HP: {e_hp})!")
            
            while e_hp > 0 and hp > 0:
                cmd = input("💥 [A]ttack or 🏃 [F]lee? ").lower()
                if cmd == "a":
                    dmg = random.randint(12, 22)
                    e_hp -= dmg
                    print(f"🗡️ You hit {enemy} for {dmg} damage.")
                    if e_hp <= 0: break
                    
                    counter = max(1, random.randint(e_atk - 3, e_atk + 3))
                    hp -= counter
                    print(f"🩸 {enemy} countered for {counter} damage.")
                elif cmd == "f" and random.random() > 0.3:
                    print("💨 Escaped back to safety!")
                    break
                elif cmd == "f":
                    print("❌ Escape blocked!")
            
            if hp <= 0:
                print(f"\n💀 {name} fell in battle at Stage {stage}. Game Over!")
                sys.exit()
            elif e_hp <= 0:
                loot = random.randint(10, 25) + (stage * 3)
                gold += loot
                stage += 1
                print(f"🏆 Defeated! Earned {loot} gold. Moving deeper...")
                
        elif act == "2":
            if gold >= 15:
                gold -= 15
                hp = min(120, hp + 60)
                print("🧪 Rested by the fire. Healed +60 HP!")
            else:
                print("❌ You lack the gold to rest.")
                
        elif act == "3":
            print(f"👋 Retiring with {gold} gold. Thanks for playing!")
            break

if __name__ == "__main__":
    main()

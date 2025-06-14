##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 08/exercise-08-17.py.py
##############################################################################
import random

print("🎮 Welcome to Alien Hunter! 👽")
print("\nChoose difficulty level:")
print("1 - Easy   (❤️  100 HP | 💥 Damage: 5-20)")
print("2 - Medium (❤️   80 HP | 💥 Damage: 10-25)")
print("3 - Hard   (❤️   75 HP | 💥 Damage: 20-30)")

while True:
    level = input("\nEnter level number (1-3): ")
    if level in ["1", "2", "3"]:
        break
    print("❌ Invalid option! Choose 1, 2, or 3.")

if level == "1":
    player_health = 100
    min_damage, max_damage = 5, 20
elif level == "2":
    player_health = 80
    min_damage, max_damage = 10, 25
else:
    player_health = 75
    min_damage, max_damage = 20, 30

tree = random.randint(1, 100)
print("\n🌳 An alien is hiding behind a tree!")
print("🔢 Each tree has been numbered from 1 to 100.")
print("❗ You have to guess which tree the alien is hiding behind.")
print("⚠️  Careful! The alien will attack you with each wrong attempt!\n")

while player_health > 0:
    print(f"❤️  Health points: {player_health}")
    guess = int(input("🎯 Choose a tree [1-100]: "))
    if guess == tree:
        print("\n🎉 CONGRATULATIONS! You got it right! The alien was found! 🎊")
        break
    elif guess > tree:
        print("⬇️  Too high! Try a lower number.")
    else:
        print("⬆️  Too low! Try a higher number.")
    damage = random.randint(min_damage, max_damage)
    player_health -= damage
    print(f"💥 The alien attacked you! Damage: {damage}\n")

if player_health <= 0:
    print("\n💀 Game Over! You didn't survive.")
    print(f"👽 The alien was behind tree {tree}.")

# Cosmos Quest damage calculator for Kryton
# Lineup: Niel lvl 1, Agatha lvl 1, WW - 99.4, Thert - 99.4, aThert - 54, Geum - 46
# Armor Aura Total: 31
# Attack Aura: 10% (applied after all other bonuses)
# Damage to Neil is done AFTER Armor is applied

neil = 150      #Neil's HP
dmg = 11        #Kryton's Base damage
amp = 10        #Kryton's amplify bonus per turn: 10 damage
geum_h = 338    #Geum's HP
geum_a = 9      #Geum's Base attack
defense = 31    #Total armor bonus applied to Geum
aura = 1.1      #Total attack aura bonus applied in percentage: 10%
t = 1           #Turn counter
total = 0       #Total damage
empowered = 1.5 #Empowered bonus: 50%

while geum_h > 0:
  print "Turn " + str(t)
  atk = int(round(geum_a * empowered * aura))
  if dmg - defense <= 0:
    k_dmg = 0
  else:
    k_dmg = dmg - defense
  if neil >= 0:
    neil = neil - round(k_dmg * .3)
    k_dmg = k_dmg - round(k_dmg * .3)
    if neil < 0:
      k_dmg = k_dmg + abs(neil)
  else:
    k_dmg = k_dmg - round(k_dmg * .3)
  print "Neil's HP: " + str(neil)
  print "Geum does " + str(atk) + " damage"
  total = total + atk
  geum_a = geum_a * 2
  print "Kryton does " + str(k_dmg) + " damage"
  geum_h = geum_h - k_dmg
  print "Geum HP: " + str(geum_h)
  dmg = dmg + 10
  t = t+1
  print '------'
print "Geum final HP: " + str(geum_h)
print "Geum final attack: " + str(geum_a)
print "Kryton final Attack: " + str(dmg)
print "Total Damage: " + str(total)
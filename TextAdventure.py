class Monster:
	
	def __init__(self, HP, MP, Atk, Def, Int, Gold, XP):
		self.HP = HP
		self.CurrentHP = HP
		self.MP = MP
		self.CurrentMP = MP
		self.Atk = Atk
		self.Def = Def
		self.Int = Int
		self.Gold = Gold
		self.XP = XP
		
	def Turn(self, target):
		if (self.currentHP/self.HP * 100) > 50:
			self.Heal()
		else:
			self.Attack(target)
	
	def Heal(self):
		print "The Monster heals itself for 5 Damage!"
		self.currentHP + 5
		if self.currentHP > self.HP:
			self.currentHP = self.HP
	
	def Attack(self, target):
		totalAtk = self.Atk - target.Def
		if totalAtk < 0:
			totalAtk = 0
		print "Monster does "+totalAtk+" damage!"
		target.HP -= totalAtk
		

 class Player:
 	
 	 def __init__(self, HP, MP, Atk, Def, Int, Gold, XP, Level):
 	 	self.HP = HP
 	 	self.currentHP = HP
 	 	self.MP = MP
 	 	self.currentMP = MP
 	 	self.Atk = Atk
 	 	self.Def = Def
 	 	self.Int = Int
 	 	self.Gold = Gold
 	 	self.XP = XP
 	 	self.Level = Level
 	 	self.spellList = ["[F]ire", "[I]ce", "[H]eal"]
 	 	
 	 def CheckXP(self):
 	 	if XP == 100:
 	 		self.LevelUp()
 	 
 	 def LevelUp(self):
 	 	
 	 	 print ("Level Up! \n")
 	 	 print ("Which do you want to increase?\n")
 	 	 choice = input("[A]tk  [I]nt")
 	 	 if choice.lower() == "a":
 	 	 	self.Atk += 2
 	 	 elif choice.lower() == "i":
 	 	 	self.Int += 2
 	 	 	
 	 	 self.HP += 5
 	 	 self.MP += 3
 	 	 self.Def += 2
 	 	 self.XP = 0
 		 self.Level += 1
 		 
 	 def Turn(self, target):
 	 	print "How would you like to act?"
 	 	choice = input("[A]ttack  [C]ast")
 	 	if choice.lower = "a":
 	 		self.Attack(target)
 	 	elif choice.lower = "c":
 	 		self.Cast(target)
 	 		
 	 			 
 	 def Attack(self, target):
 	 	totalAtk = self.Atk - target.Def
 	 	if totalAtk < 0:
 	 		totalAtk = 0
 	 	print "You do "+totalAtk+" Damage to the monster"		target.currentHP -= totalAtk
 	 		 
 	 def Cast(self, target):
 	 	print "What do you want to cast?"
 	 	choice = input(self.spellList)
 	 	if choice.lower() = "f":
 	 		self.Fire(target)
 	 	elif choice.lower() = "i":
 	 		self.Ice(target)
 	 	elif choice.lower = "h":
 	 		self.Heal()
 	 
 	 def Fire(self, target):
 	 	if self.currentMP < 4:
 	 		print "The spell fizzles as you do not have enough power to cast it"
 	 	else:
 	 		fireDam = self.Int * 2
 	 		print "You cast a fireball at the monster dealing "+fireDam+" damage to it"
 	 		target.currentHP -= fireDam
 	 		self.currentMP -= 4
 	 
 	 def Ice(self, target):
 	 	if self.currentMP < 2:
 	 		print "The spell fizzles as you do not have enough power to cast it"		else:
 	 		iceDam = self.Int
 	 		print "You cast a spear of ice at the target dealing "+iceDam+" damage to it"			target.currentHP -= iceDam
 	 		self.currentMP -= 2
 	 		
 	 def Heal(self):
 	 	if self.currentMP < 3:
 	 		print "The spell fizzles as you do not have enough power to cast it"
 	 		
 	 	else:
 	 		print "You cast a healing glow restoring 5 health to yourself"
 	 		self.currentHP += 5
 
def printBattle(Player, Monster):
	print """---------------------------
	|Monster : HP = %d MP = %d| 
	---------------------------
	|                         |
	|                         |
	|                         |
	---------------------------
	|Player : HP = %d MP = %d |
	---------------------------""" % (Monster.currentHP, Monster.currentMP, Player.currentHP, player.currentMP)
	
def battleLoop(Player, Monster):
	print "A Monster has attacked!!"
	gameLoop = True
	printBattle(Player, Monster)
	while gameLoop == True:
		Player.Turn()
		if Monster.currentHP >= 0:
		
			Monster.Turn() 	
			
		else:
			gameLoop = False
		
		if Player.currentHP <= 0:
			gameLoop = False
		printBattle(Player, Monster)

def main():
	Player = 

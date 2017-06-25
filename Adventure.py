

class Monster:
	
	def __init__(self, HP, MP, Atk, Def, Int, Gold, XP):
		self.HP = HP
		self.currentHP = HP
		self.MP = MP
		self.currentMP = MP
		self.Atk = Atk
		self.Def = Def
		self.Int = Int
		self.Gold = Gold
		self.XP = XP
		
	def Turn(self, target):
		if (self.currentHP/self.HP * 100) < 50:
			self.Heal()
		else:
			self.Attack(target)
	
	def Heal(self):
		print "The Monster heals itself for 5 Damage!\n"
		self.currentHP + 5
		if self.currentHP > self.HP:
			self.currentHP = self.HP
	
	def Attack(self, target):
		totalAtk = self.Atk - target.Def
		if totalAtk < 0:
			totalAtk = 0
		print "Monster does "+str(totalAtk)+" damage!\n"
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
 	 	self.Inventory = {}
		
 	 def CheckXP(self):
 	 	if XP == 100:
 	 		self.LevelUp()
 	 
 	 def LevelUp(self):
 	 	
 	 	 print ("Level Up! \n")
 	 	 print ("Which do you want to increase?\n")
 	 	 choice = raw_input("[A]tk  [I]nt\n")
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
 	 	print "How would you like to act?\n"
 	 	choice = raw_input("[A]ttack  [C]ast\n")
 	 	if choice.lower() == "a":
 	 		return self.Attack(target)
 	 	elif choice.lower() == "c":
 	 		return self.Cast(target)
 	 		
 	 			 
 	 def Attack(self, target):
 	 	totalAtk = self.Atk - target.Def
 	 	if totalAtk < 0:
 	 		totalAtk = 0
 	 	print "You do "+str(totalAtk)+" Damage to the monster\n"		
		target.currentHP -= totalAtk
 	 	return False
	 
 	 def Cast(self, target):
 	 	print "What do you want to cast?\n"
 	 	choice = raw_input(self.spellList)
 	 	if choice.lower() == "f":
 	 		return self.Fire(target)
 	 	elif choice.lower() == "i":
 	 		return self.Ice(target)
 	 	elif choice.lower() == "h":
 	 		return self.Heal()
 	 
 	 def Fire(self, target):
 	 	if self.currentMP < 4:
 	 		print "The spell fizzles as you do not have enough power to cast it\n"
			return True
			
 	 	else:
 	 		fireDam = self.Int * 2
 	 		print "You cast a fireball at the monster dealing "+str(fireDam)+" damage to it\n"
 	 		target.currentHP -= fireDam
 	 		self.currentMP -= 4
 	 		return False
 	 def Ice(self, target):
 	 	if self.currentMP < 2:
 	 		print "The spell fizzles as you do not have enough power to cast it\n"			
			return True
		else:
 	 		iceDam = self.Int
 	 		print "You cast a spear of ice at the target dealing "+str(iceDam)+" damage to it\n"
			
			target.currentHP -= iceDam
 	 		self.currentMP -= 2
 	 		return False
 	 def Heal(self):
 	 	if self.currentMP < 3:
 	 		print "The spell fizzles as you do not have enough power to cast it\n"
 	 		return True
 	 	else:
 	 		print "You cast a healing glow restoring 5 health to yourself\n"
 	 		self.currentHP += 5
			if self.currentHP > self.HP:
				self.currentHP = self.HP
			self.currentMP -= 3
 			return False
class Item:

	def __init__(self, Name, Cost):
		
		self.Name = Name
		self.Cost = Cost


	def itemUse(self, User):
		##This will determine what the item does when used from the inventory
		return
	def battleUse(self, User, Target):
		##This is for items when used in battle
		return

def printBattle(Player, Monster):
	print """---------------------------
|Monster : HP = %d MP = %d| 
---------------------------
|                         |
|                         |
|                         |
---------------------------
|Player : HP = %d MP = %d |
---------------------------\n""" % (Monster.currentHP, Monster.currentMP, Player.currentHP, Player.currentMP)
	
def battleLoop(Player, Monster):
	print "A Monster has attacked!!\n"
	gameLoop = True

	printBattle(Player, Monster)
	while gameLoop == True:
		playerTurn = True
		while playerTurn == True:

			playerTurn = Player.Turn(Monster)
		if Monster.currentHP > 0:
		
			Monster.Turn(Player) 	
			
		else:
			gameLoop = False
		
		if Player.currentHP <= 0:
			gameLoop = False
		printBattle(Player, Monster)

def main():
	player = Player(50, 30, 10, 5, 10, 0, 0, 1)
	monster = Monster(50, 30, 5, 5, 5, 0, 0)
	battleLoop(player, monster)
	
if __name__ == "__main__":
	main()
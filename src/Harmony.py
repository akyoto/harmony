####################################################################
# Header
####################################################################
# Harmony
# 
# Website: www.blitzprog.com
# Started: 28.11.2010 (Sun, Nov 28 2010)

####################################################################
# License
####################################################################
# (C) 2010  Eduard Urbach
# 
# This file is part of Harmony.
# 
# Harmony is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Harmony is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with Harmony. If not, see <http://www.gnu.org/licenses/>.

#  ____________________
# | |#||#| | |#||#||#| |
# | |#||#| | |#||#||#| |
# | |_||_| | |_||_||_| |
# |  |  |  |  |  |  |  |
# |__|__|__|__|__|__|__|

#    des es      ges as  bes
#  __cis_dis_____fis_gis_ais__
# |  |#| |#|  |  |#| |#| |#|  |
# |  |#| |#|  |  |#| |#| |#|  |
# |  |_| |_|  |  |_| |_| |_|  |
# |   |   |   |   |   |   |   |
# |_C_|_D_|_E_|_F_|_G_|_A_|_B_|

# C-Dur:
#   2   2   1   2   2   2   1
# D-Moll:
#       2   1   2   2   1   3   1
# a-moll: (natürlich)
# 2, 1, 2, 2, 1, 2, 2
#                3, 1 (harmonisch)
#             2, 2, 1 (melodisch)
        
# d, e, f, g, a, bes, cis

# Quinten:
# 	Up:
# 		C -> G -> D -> A -> E -> B -> F
# 	Down:
# 		C -> F -> B -> E -> A -> D -> G

#            C
#        /       \
#       F         G
#       |         |
#       B         D
#        \       /
#         E --- A

####################################################################
# Imports
####################################################################
from Utils import *

####################################################################
# Const
####################################################################
MAJOR = 1
MINOR = 0
separator = " | "

tones = []
tones.append("c")		# 0
tones.append("cis")		# 1
tones.append("d")		# 2
tones.append("dis")		# 3
tones.append("e")		# 4
tones.append("f")		# 5
tones.append("fis")		# 6
tones.append("g")		# 7
tones.append("gis")		# 8
tones.append("a")		# 9
tones.append("ais")		# 10
tones.append("b")		# 11

####################################################################
# Classes
####################################################################
# getHalfToneName
def getHalfToneName(halfTone):
	postfix = halfTone // 12
	if postfix:
		return tones[halfTone % 12] + str(postfix)
	else:
		return tones[halfTone % 12]
	
# getHalfToneByName
def getHalfToneByName(name):
	for i in range(12):
		if tones[i] == name:
			return i
	return ""

# KeyList
class KeyList:
	def __init__(self):
		self.keys = 	{
							"C" : Key(0, MAJOR),
							"Cm" : Key(0, MINOR),
							"D" : Key(2, MAJOR),
							"Dm" : Key(2, MINOR)
						}
	
	def printChords(self, halfTone):
		for key in self.keys.items():
			key[1].printChords(halfTone)
	
	def __getitem__(self, keyName):
		return self.keys[keyName]
	
# Key
class Key:
	def __init__(self, halfToneOffset, isMajor):
		self.halfToneOffset = halfToneOffset
		self.isMajor = isMajor
		
		if self.isMajor:
			self.majors = [MAJOR, MINOR, MINOR, MAJOR, MAJOR, MINOR, MINOR]
		else:
			self.majors = [MINOR, MAJOR, MAJOR, MINOR, MINOR, MAJOR, MAJOR]
		
	def __add__(self, num):
		return Key(self.halfToneOffset + num, self.isMajor)
		
	def getStufeTriad(self, stufe):
		# TODO: Stufenberechnung
		return Triad(self.halfToneOffset + stufe, self.halfToneOffset + stufe + 3 + self.majors[stufe], self.halfToneOffset + stufe + 4 + 3)
	
	def printChords(self, halfTone):
		for i in range(7):
			triad = self.getStufeTriad(i)
			if triad.contains(halfTone):
				print(getHalfToneName(self.halfToneOffset) + " " + ["minor", "major"][self.isMajor] + " [" + str(i + 1) + "]: " + str(triad))
	
# Triad
class Triad:
	def __init__(self, a, b, c):
		self.halfTones = (a, b, c)
		
	def contains(self, halfTone):
		return self.halfTones[0] == halfTone or self.halfTones[1] == halfTone or self.halfTones[2] == halfTone
		
	def __add__(self, num):
		return Triad(self.halfTones[0] + num, self.halfTones[1] + num, self.halfTones[2] + num)
		
	def __sub__(self, num):
		return Triad(self.halfTones[0] - num, self.halfTones[1] - num, self.halfTones[2] - num)
		
	def __str__(self):
		return getHalfToneName(self.halfTones[0]) + separator + getHalfToneName(self.halfTones[1]) + separator + getHalfToneName(self.halfTones[2])

####################################################################
# Main
####################################################################
if __name__ == '__main__':
	try:
		myInput = "d"
		halfTone = getHalfToneByName(myInput)
		
		keyList = KeyList()
		keyList.printChords(halfTone)
	except:
		printTraceback()

class carro:
	def __init__ (self,gasolina,hp):
		self.hp = hp
		self.gasolina = gasolina
		self.enmarcha = False
		print "tenemos",gasolina,"litros de gasolina y",hp,"de hp."
	def conduce(self):
		if self.enmarcha == True:
			if self.gasolina > 0:
				self.gasolina -= self.hp/100
				print "quedan",self.gasolina,"litros"
			else:
				self.enmarcha = False
				print "No gasolina"
		else:
			print "Tienes que poner el carro en marcha"
	def arrancar(self):
		if self.gasolina > 0:
			self.enmarcha = True
			print "En marcha"
		else:
			self.enmarcha = False
			print "No arranca (no gasolina)"

def hola(texto):
	print texto

print "hola"
Input = raw_input('introduce algo')

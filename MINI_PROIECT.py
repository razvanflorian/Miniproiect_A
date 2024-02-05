
class Masina:
    def __init__(self, model, viteza_maxima, marca, culori_disponibile, inmatriculata=False):
        self.marca = marca
        self.model = model
        self.viteza_maxima = viteza_maxima
        self.viteza_actuala = 0
        self.culoare = "gri"
        self.culori_disponibile = culori_disponibile
        self.inmatriculata = inmatriculata

    def descrie(self):
        print(f"Marca: {self.marca}")
        print(f"Model: {self.model}")
        print(f"Viteza Maxima: {self.viteza_maxima}")
        print(f"Viteza Actuala: {self.viteza_actuala}")
        print(f"Culoare: {self.culoare}")
        print(f"Inmatriculata: {self.inmatriculata}")

    def inmatriculare(self):
        self.inmatriculata = True

    def vopseste(self, culoare):
        if culoare in self.culori_disponibile:
            self.culoare = culoare
            print(f"Mașina a fost vopsită în culoarea {culoare}.")
        else:
            print(f"Nu se poate vopsi mașina în culoarea {culoare}, culoarea nu este disponibilă.")

    def accelereaza(self, viteza):
        if viteza < 0:
            print("Eroare: Viteza nu poate fi negativă.")
        elif viteza <= self.viteza_maxima:
            self.viteza_actuala = viteza
        else:
            self.viteza_actuala = self.viteza_maxima
            print(f"Mașina a atins viteza maximă de {self.viteza_maxima}.")

    def franeaza(self):
        self.viteza_actuala = 0
        print("Mașina s-a oprit.")

# Exemplu de utilizare:
culori_disponibile = ["rosu", "albastru", "negru", "verde", "alb"]
masina_mea = Masina(model="Sedan", viteza_maxima=200, marca="Toyota", culori_disponibile=culori_disponibile)

masina_mea.descrie()
masina_mea.inmatriculare()
masina_mea.vopseste("albastru")
masina_mea.accelereaza(180)
masina_mea.accelereaza(220)
masina_mea.franeaza()




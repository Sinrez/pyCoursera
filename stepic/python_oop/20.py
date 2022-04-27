class UnitedKingdom:
    def capital(self):
        print("London is the capital of Great Britain.")

    def language(self):
        print("English is the primary language of Great Britain.")

class Spain:
    def capital(self):
        print("Madrid is the capital of Spain.")

    def language(self):
        print("Spanish is the primary language of Spain.")


obj_uk = UnitedKingdom()
obj_spa = Spain()
for country in (obj_spa, obj_uk):
    country.capital()
    country.language()
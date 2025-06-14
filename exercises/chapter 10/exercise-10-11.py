##############################################################################
# Python From Scratch
# Author: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2025 - LogiKraft 2025
# Site: https://pythonfromscratch.com
# ISBN: 978-85-7522-949-1 (Paperback), 978-85-7522-950-7 (hardcover), 978-85-7522-951-4 (ebook)
#
# File: chapter 10/exercise-10-11.py.py
##############################################################################
class State:
    def __init__(self, name, acronym):
        self.name = name
        self.acronym = acronym
        self.cities = []

    def add_city(self, city):
        city.state = self
        self.cities.append(city)

    def population(self):
        return sum([c.population for c in self.cities])


class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population
        self.state = None

    def __str__(self):
        return (
            f"City (name={self.name}, population={self.population}, state={self.state})"
        )


# Populations obtained from Wikipedia
# IBGE 2012 estimate
am = State("Amazonas", "AM")
am.add_city(City("Manaus", 1861838))
am.add_city(City("Parintins", 103828))
am.add_city(City("Itacoatiara", 89064))

sp = State("São Paulo", "SP")
sp.add_city(City("São Paulo", 11376685))
sp.add_city(City("Guarulhos", 1244518))
sp.add_city(City("Campinas", 1098630))

rj = State("Rio de Janeiro", "RJ")
rj.add_city(City("Rio de Janeiro", 6390290))
rj.add_city(City("São Gonçalo", 1016128))
rj.add_city(City("Duque de Caixias", 867067))


for state in [am, sp, rj]:
    print(f"State: {state.name} Acronym: {state.acronym}")
    for city in state.cities:
        print(f"City: {city.name} Population: {city.population}")
    print(f"State Population: {state.population()}\n")

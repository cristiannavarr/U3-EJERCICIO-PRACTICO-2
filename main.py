from pokemon import Pokemon
from battle_system import BattleSystem
import pandas as pd
import os

class PokemonManager:
    def __init__(self):
        self.pokemons = []
        self.load_pokemons_from_csv()
    
    def load_pokemons_from_csv(self):
        """Carga Pokémon desde el archivo CSV con toda la información"""
        try:
            data = pd.read_csv('data/pokemon.csv')
            for _, row in data.iterrows():
                # Recoger habilidades
                abilities = []
                if pd.notna(row.get('ability_1')):
                    abilities.append(row['ability_1'])
                if pd.notna(row.get('ability_2')):
                    abilities.append(row['ability_2'])
                
                pokemon = Pokemon(
                    name=row['name'],
                    type_1=row['type_1'],
                    type_2=row['type_2'],
                    hp=row['hp'],
                    attack=row['attack'],
                    defense=row['defense'],
                    sp_attack=row['sp_attack'],
                    sp_defense=row['sp_defense'],
                    speed=row['speed'],
                    generation=row.get('generation'),
                    species=row.get('species'),
                    height=row.get('height_m'),
                    weight=row.get('weight_kg'),
                    abilities=abilities
                )
                self.pokemons.append(pokemon)
            print(f"Se cargaron {len(self.pokemons)} Pokémon")
        except FileNotFoundError:
            print("Archivo pokemon.csv no encontrado")
    
    def show_pokemons(self):
        """Muestra todos los Pokémon disponibles"""
        print("\n--- Pokémon Disponibles ---")
        for i, pokemon in enumerate(self.pokemons, 1):
            print(f"{i}. {pokemon}")
    
    def show_pokemon_details(self):
        """Muestra información detallada de un Pokémon específico"""
        self.show_pokemons()
        try:
            index = int(input("\nNúmero del Pokémon para ver detalles: ")) - 1
            if 0 <= index < len(self.pokemons):
                pokemon = self.pokemons[index]
                print(pokemon.get_detailed_info())
            else:
                print("Número inválido")
        except ValueError:
            print("Por favor ingresa un número válido")
    
    def modify_pokemon(self):
        """Modifica las características de un Pokémon existente"""
        self.show_pokemons()
        try:
            index = int(input("\nNúmero del Pokémon a modificar: ")) - 1
            if 0 <= index < len(self.pokemons):
                pokemon = self.pokemons[index]
                print(f"\nModificando: {pokemon.name}")
                print(pokemon.get_detailed_info())
                
                while True:
                    print("\n--- ¿Qué quieres modificar? ---")
                    print("1. Nombre")
                    print("2. HP")
                    print("3. Ataque")
                    print("4. Defensa")
                    print("5. Ataque Especial")
                    print("6. Defensa Especial")
                    print("7. Velocidad")
                    print("8. Altura")
                    print("9. Peso")
                    print("10. Terminar modificación")
                    
                    choice = input("\nSelecciona una opción: ")
                    
                    if choice == '1':
                        new_name = input("Nuevo nombre: ")
                        pokemon.name = new_name
                        print("Nombre actualizado")
                    
                    elif choice == '2':
                        new_hp = int(input("Nuevo HP: "))
                        pokemon.hp = new_hp
                        print("HP actualizado")
                    
                    elif choice == '3':
                        new_attack = int(input("Nuevo ataque: "))
                        pokemon.attack = new_attack
                        print("Ataque actualizado")
                    
                    elif choice == '4':
                        new_defense = int(input("Nueva defensa: "))
                        pokemon.defense = new_defense
                        print("Defensa actualizada")
                    
                    elif choice == '5':
                        new_sp_attack = int(input("Nuevo ataque especial: "))
                        pokemon.sp_attack = new_sp_attack
                        print("Ataque especial actualizado")
                    
                    elif choice == '6':
                        new_sp_defense = int(input("Nueva defensa especial: "))
                        pokemon.sp_defense = new_sp_defense
                        print("Defensa especial actualizada")
                    
                    elif choice == '7':
                        new_speed = int(input("Nueva velocidad: "))
                        pokemon.speed = new_speed
                        print("Velocidad actualizada")
                    
                    elif choice == '8':
                        new_height = float(input("Nueva altura (metros): "))
                        pokemon.height = new_height
                        print("Altura actualizada")
                    
                    elif choice == '9':
                        new_weight = float(input("Nuevo peso (kg): "))
                        pokemon.weight = new_weight
                        print("Peso actualizado")
                    
                    elif choice == '10':
                        print("Modificaciones terminadas")
                        break
                    
                    else:
                        print("Opción inválida")
                
                print(f"\n{pokemon.name} ha sido actualizado:")
                print(pokemon.get_detailed_info())
            
            else:
                print("Número inválido")
        
        except ValueError:
            print("Por favor ingresa un número válido")
    
    def add_pokemon(self):
        """Agrega un nuevo Pokémon manualmente"""
        print("\n--- Agregar Nuevo Pokémon ---")
        name = input("Nombre: ")
        type_1 = input("Tipo principal: ")
        type_2 = input("Tipo secundario (opcional): ") or None
        
        # Estadísticas básicas
        hp = int(input("HP (número): "))
        attack = int(input("Ataque (número): "))
        defense = int(input("Defensa (número): "))
        sp_attack = int(input("Ataque especial (número): "))
        sp_defense = int(input("Defensa especial (número): "))
        speed = int(input("Velocidad (número): "))
        
        # Información adicional
        species = input("Especie (opcional): ") or None
        generation = input("Generación (opcional): ") or None
        height = input("Altura en metros (opcional, número): ") or None
        weight = input("Peso en kg (opcional, número): ") or None
        
        if height:
            height = float(height)
        if weight:
            weight = float(weight)
        
        new_pokemon = Pokemon(
            name=name, type_1=type_1, type_2=type_2,
            hp=hp, attack=attack, defense=defense,
            sp_attack=sp_attack, sp_defense=sp_defense, speed=speed,
            species=species, generation=generation,
            height=height, weight=weight
        )
        
        self.pokemons.append(new_pokemon)
        print(f"¡{name} agregado exitosamente!")
    
    def delete_pokemon(self):
        """Elimina un Pokémon"""
        self.show_pokemons()
        try:
            index = int(input("\nNúmero del Pokémon a eliminar: ")) - 1
            if 0 <= index < len(self.pokemons):
                removed = self.pokemons.pop(index)
                print(f"¡{removed.name} eliminado!")
            else:
                print("Número inválido")
        except ValueError:
            print("Por favor ingresa un número válido")

def main():
    manager = PokemonManager()
    battle_system = BattleSystem()
    
    while True:
        print("\n" + "="*50)
        print("          SISTEMA DE BATALLAS POKÉMON")
        print("="*50)
        print("1. Ver lista de Pokémon")
        print("2. Ver detalles de un Pokémon")
        print("3. Agregar Pokémon")
        print("4. Modificar Pokémon")
        print("5. Eliminar Pokémon")
        print("6. Batalla")
        print("7. Salir")
        
        choice = input("\nSelecciona una opción: ")
        
        if choice == '1':
            manager.show_pokemons()
        
        elif choice == '2':
            manager.show_pokemon_details()
        
        elif choice == '3':
            manager.add_pokemon()
        
        elif choice == '4':
            manager.modify_pokemon()
        
        elif choice == '5':
            manager.delete_pokemon()
        
        elif choice == '6':
            if len(manager.pokemons) < 2:
                print("Necesitas al menos 2 Pokémon para una batalla")
                continue
            
            manager.show_pokemons()
            try:
                print("\n--- Selecciona dos Pokémon para la batalla ---")
                p1_index = int(input("Primer Pokémon: ")) - 1
                p2_index = int(input("Segundo Pokémon: ")) - 1
                
                if (0 <= p1_index < len(manager.pokemons) and 
                    0 <= p2_index < len(manager.pokemons) and 
                    p1_index != p2_index):
                    
                    pokemon1 = manager.pokemons[p1_index]
                    pokemon2 = manager.pokemons[p2_index]
                    
                    winner = battle_system.battle(pokemon1, pokemon2)
                    
                else:
                    print("Selección inválida")
            
            except ValueError:
                print("Por favor ingresa números válidos")
        
        elif choice == '7':
            print("¡Juego Finalizado!")
            break
        
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()
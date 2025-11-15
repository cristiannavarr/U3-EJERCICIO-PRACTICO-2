import random

class BattleSystem:
    def __init__(self):
        # Tabla de efectividad básica
        self.type_chart = {
            'Fire': {'Grass': 2.0, 'Water': 0.5},
            'Water': {'Fire': 2.0, 'Grass': 0.5},
            'Grass': {'Water': 2.0, 'Fire': 0.5},
            'Electric': {'Water': 2.0},
            'Fighting': {'Normal': 2.0},
            'Psychic': {'Fighting': 2.0},
            'Ghost': {'Psychic': 2.0},
            'Dragon': {'Dragon': 2.0}
        }
    
    def calculate_damage(self, attacker, defender):
        """Calcula el daño"""
        # Daño base usando el ataque del Pokémon
        base_damage = attacker.attack
        
        # Multiplicador por tipo (usando el tipo principal del atacante vs defensor)
        effectiveness = 1.0
        attacker_type = attacker.type_1
        defender_types = defender.get_types()
        
        for defender_type in defender_types:
            if attacker_type in self.type_chart and defender_type in self.type_chart[attacker_type]:
                effectiveness *= self.type_chart[attacker_type][defender_type]
        
        # Cálculo final
        damage = (base_damage * effectiveness) // 2
        
        # Mensajes de efectividad
        if effectiveness > 1:
            print("\n¡El ataque es efectivo! (se dobla x2)")
        elif effectiveness < 1:
            print("\nEl ataque no es efectivo... (se reduce al a mitad x0.5)")
        
        return max(1, damage)  # Mínimo 1 de daño
    
    def battle(self, pokemon1, pokemon2):
        """Simula una batalla"""
        print(f"\n¡Comienza la batalla!")
        print(f"\n{pokemon1.name} vs {pokemon2.name}")
        print("")
        print("-" * 30)
        
        # Restaurar HP antes de la batalla
        pokemon1.restore_health()
        pokemon2.restore_health()
        
        turn = 0
        while not pokemon1.is_fainted() and not pokemon2.is_fainted():
            turn += 1
            print("")
            print(f"\n--- Turno {turn} ---")
            
            # Quién ataca primero (por velocidad)
            first, second = (pokemon1, pokemon2) if pokemon1.speed >= pokemon2.speed else (pokemon2, pokemon1)
            
            # Primer ataque
            damage = self.calculate_damage(first, second)
            second.take_damage(damage)
            print("")
            print(f"{first.name} ataca - Daño: {damage}")
            print(f"{second.name} HP: {second.current_hp}/{second.hp}")
            
            if second.is_fainted():
                print(f"\n¡{first.name} gana la batalla!")
                print(f"Turnos: {turn}")
                return first
            
            # Segundo ataque
            damage = self.calculate_damage(second, first)
            first.take_damage(damage)
            print("")
            print(f"{second.name} ataca - Daño: {damage}")
            print(f"{first.name} HP: {first.current_hp}/{first.hp}")
            
            if first.is_fainted():
                print(f"\n¡{second.name} gana la batalla!")
                print(f"Turnos: {turn}")
                return second
        
        return None
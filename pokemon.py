import pandas as pd

class Pokemon:
    def __init__(self, name, type_1, type_2, hp, attack, defense, sp_attack, sp_defense, speed, 
                 generation=None, species=None, height=None, weight=None, abilities=None):
        self.name = name
        self.type_1 = type_1
        self.type_2 = type_2 if pd.notna(type_2) else None
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.sp_attack = sp_attack
        self.sp_defense = sp_defense
        self.speed = speed
        self.current_hp = hp
        
        # Nuevas características
        self.generation = generation
        self.species = species
        self.height = height
        self.weight = weight
        self.abilities = abilities or []
    
    def get_types(self):
        """Devuelve los tipos del Pokémon como lista"""
        types = [self.type_1]
        if self.type_2:
            types.append(self.type_2)
        return types
    
    def take_damage(self, damage):
        """Reduce el HP del Pokémon"""
        self.current_hp -= damage
        if self.current_hp < 0:
            self.current_hp = 0
    
    def is_fainted(self):
        """Verifica si el Pokémon está debilitado"""
        return self.current_hp <= 0
    
    def restore_health(self):
        """Restaura el HP al máximo"""
        self.current_hp = self.hp
    
    def get_detailed_info(self):
        """Devuelve información detallada del Pokémon"""
        info = f"""
=== TARJETA POKÉMON: {self.name} ===
    Especie: {self.species or 'No especificada'}
    Generación: {self.generation or 'No especificada'}
    Tipos: {', '.join(self.get_types())}

   Características Físicas:
   - Altura: {self.height or 'No especificada'} m
   - Peso: {self.weight or 'No especificada'} kg

   Estadísticas de Combate:
   - HP: {self.hp}
   - Ataque: {self.attack}
   - Defensa: {self.defense}
   - Ataque Especial: {self.sp_attack}
   - Defensa Especial: {self.sp_defense}
   - Velocidad: {self.speed}

    Habilidades: {', '.join(self.abilities) if self.abilities else 'No especificadas'}
"""
        return info
    
    def __str__(self):
        types = "/".join(self.get_types())
        return f"{self.name} ({types}) - HP: {self.hp} | ATK: {self.attack} | DEF: {self.defense}"
from math import ceil, floor

import config
from error import BadNewWorm, NotEnoughFood, MaxLengthReached, CannotDivide, DividedWorm, DeadWorm


class Worm:
    """Simple worm simulation."""

    # Shared food.
    food = config.food

    def __init__(self, length=config.length, energy=config.energy):
        if length <= 0 or energy <= 0:
            raise BadNewWorm(length=length, energy=energy)
        self.alive = True
        self.divided = False
        self.age = 0
        self.length = length
        self.energy = energy

    def checks(method):
        def wrapper(self, *args, **kwargs):
            self._is_alive()
            method(self, *args, **kwargs)
            self._get_older()
        return wrapper

    @checks
    def eat(self, units=1):
        if type(self).food < units:
            raise NotEnoughFood(food=type(self).food, eat=units)
        type(self).food -= units
        self.energy += units * config.energy_per_food

    @checks
    def dig(self):
        type(self).food += config.food_per_dig
        self.energy -= config.energy_per_dig

    @checks
    def grow(self):
        self.energy -= 1
        if self.length < config.max_length:
            self.length += config.length_per_energy
        else:
            raise MaxLengthReached(length=self.length)

    def divide(self):
        self._is_alive()
        if self.length >= 2 and self.energy >= 2 and self.age >= config.fertility_age:
            self.divided = True
            self.alive = False
            half_length = self.length / 2
            half_energy = self.energy / 2
            new_lengths = (floor(half_length), ceil(half_length))
            new_energies = (ceil(half_energy), floor(half_energy))
            return [type(self)(length, energy) for length, energy in zip(new_lengths, new_energies)]
        else:
            raise CannotDivide(length=self.length, energy=self.energy, age=self.age)

    def _is_alive(self):
        if not self.alive:
            if self.divided:
                raise DividedWorm()
            else:
                raise DeadWorm()

    def _get_older(self):
        self.age += 1
        if self.energy <= 0:
            self.alive = False

#!/usr/bin/python
# -*- coding: utf-8 -*-

class MLEngineer:

    def __init__(self):
        self.name = "Andrei Solot"
        self.role = "Machine Learning Engineer"
        self.language_spoken = ("ro_RO", "en_GB", "it_IT")

    def say_hi(self):
        print("Thanks for dropping by, hope you find some of my work interesting.")


me = MLEngineer()
me.say_hi()

"""Desafio 021 - Faça um programa em python que abra e reproduza o audio de um arquivo MP3"""
# Obs.: O programa só funciona caso o arquivo seja baixado e colocado na mesma pasta do script.
import pygame

input('pressione enter para ouvir o aviso: ')
pygame.init()
pygame.mixer.music.load('agarra.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
input('Pressione enter para finalizar.')
pygame.event.wait(0)

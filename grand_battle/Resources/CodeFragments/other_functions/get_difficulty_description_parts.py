import pygame

from grand_battle.Resources.CodeFragments.other_functions import get_font


def get_beginner_difficulty_description_parts(Button_config):
    description_text_parts = []
    description_rect_parts = []

    description_text_parts.append(get_font(Button_config.DESCRIPTION_FONT_SIZE).render(
                        "Beginner difficulty (I'm Too Young to Die):", True, "#605b00"))
    description_rect_parts.append(description_text_parts[0].get_rect(center=(672, 518)))
    Button_config.SCREEN.blit(description_text_parts[0], description_rect_parts[0])

    description_text_parts.append(get_font(Button_config.DESCRIPTION_FONT_SIZE).render(
                        "- Guaranteed drop from every enemy", True, "#605b00"))
    description_rect_parts.append(description_text_parts[1].get_rect(center=(710, 550)))
    Button_config.SCREEN.blit(description_text_parts[1], description_rect_parts[1])

    description_text_parts.append(get_font(Button_config.DESCRIPTION_FONT_SIZE).render(
                        "Beginner difficulty (I'm Too Young to Die):", True, "#605b00"))
    description_rect_parts.append(description_text_parts[2].get_rect(center=(710, 585)))
    Button_config.SCREEN.blit(description_text_parts[2], description_rect_parts[2])

    description_text_parts.append(get_font(Button_config.DESCRIPTION_FONT_SIZE).render(
                        "Beginner difficulty (I'm Too Young to Die):", True, "#605b00"))
    description_rect_parts.append(description_text_parts[3].get_rect(center=(655, 620)))
    Button_config.SCREEN.blit(description_text_parts[3], description_rect_parts[3])
    beginner_difficulty = pygame.image.load("Textures/beginner_difficulty_icon.png")
    Button_config.SCREEN.blit(beginner_difficulty, (420, 550))


def get_medium_difficulty_description_parts(Button_config):
    description_text_parts = []
    description_rect_parts = []
    description_text_parts.append(get_font(Button_config.DESCRIPTION_FONT_SIZE).render(
                        "Medium difficulty (Hurt Me Plenty):", True, "#605b00"))
    description_rect_parts.append(description_text_parts[0].get_rect(center=(672, 518)))
    Button_config.SCREEN.blit(description_text_parts[0], description_rect_parts[0])

    description_text_parts.append(get_font(Button_config.DESCRIPTION_FONT_SIZE).render(
                        "- 70% chance of drop from every enemy", True, "#605b00"))
    description_rect_parts.append(description_text_parts[1].get_rect(center=(725, 550)))
    Button_config.SCREEN.blit(description_text_parts[1], description_rect_parts[1])

    description_text_parts.append(get_font(Button_config.DESCRIPTION_FONT_SIZE).render(
                        "   - 2 additional lifes in every attempt", True, "#605b00"))
    description_rect_parts.append(description_text_parts[2].get_rect(center=(710, 585)))
    Button_config.SCREEN.blit(description_text_parts[2], description_rect_parts[2])

    description_text_parts.append(get_font(Button_config.DESCRIPTION_FONT_SIZE).render(
                        "   - Normal reaction of", True, "#605b00"))
    description_rect_parts.append(description_text_parts[3].get_rect(center=(625, 620)))
    Button_config.SCREEN.blit(description_text_parts[3], description_rect_parts[3])

    description_text_parts.append(get_font(Button_config.DESCRIPTION_FONT_SIZE).render(
                        "turrets and bullets speed", True, "#605b00"))
    description_rect_parts.append(description_text_parts[4].get_rect(center=(665, 655)))
    Button_config.SCREEN.blit(description_text_parts[4], description_rect_parts[4])

    medium_difficulty = pygame.image.load("Textures/medium_difficulty_icon.png")
    Button_config.SCREEN.blit(medium_difficulty, (420, 550))


def get_hard_difficulty_description_parts(Button_config):
    description_text_parts = []
    description_rect_parts = []
    description_text_parts.append(get_font(Button_config.DESCRIPTION_FONT_SIZE).render(
                        "Hard difficulty (Ultra Violence):", True, "#605b00"))
    description_rect_parts.append(description_text_parts[0].get_rect(center=(672, 518)))
    Button_config.SCREEN.blit(description_text_parts[0], description_rect_parts[0])

    description_text_parts.append(get_font(Button_config.DESCRIPTION_FONT_SIZE).render(
                        "- 30% chance of drop from every enemy", True, "#605b00"))
    description_rect_parts.append(description_text_parts[1].get_rect(center=(725, 550)))
    Button_config.SCREEN.blit(description_text_parts[1], description_rect_parts[1])

    description_text_parts.append(get_font(Button_config.DESCRIPTION_FONT_SIZE).render(
                        "   - 1 additional lifes in every attempt", True, "#605b00"))
    description_rect_parts.append(description_text_parts[2].get_rect(center=(710, 585)))
    Button_config.SCREEN.blit(description_text_parts[2], description_rect_parts[2])

    description_text_parts.append(get_font(Button_config.DESCRIPTION_FONT_SIZE).render(
                        "   - Very fast reaction of", True, "#605b00"))
    description_rect_parts.append(description_text_parts[3].get_rect(center=(640, 620)))
    Button_config.SCREEN.blit(description_text_parts[3], description_rect_parts[3])

    description_text_parts.append(get_font(Button_config.DESCRIPTION_FONT_SIZE).render(
                        "turrets and bullets speed", True, "#605b00"))
    description_rect_parts.append(description_text_parts[4].get_rect(center=(665, 655)))
    Button_config.SCREEN.blit(description_text_parts[4], description_rect_parts[4])
    hard_difficulty = pygame.image.load("Textures/hard_difficulty_icon.png")
    Button_config.SCREEN.blit(hard_difficulty, (420, 550))


def get_insane_difficulty_description_parts(Button_config):
    description_text_parts = []
    description_rect_parts = []
    description_text_parts.append(get_font(Button_config.DESCRIPTION_FONT_SIZE).render(
                        "Insane difficulty (Nightmare):", True, "#605b00"))
    description_rect_parts.append(description_text_parts[0].get_rect(center=(672, 518)))
    Button_config.SCREEN.blit(description_text_parts[0], description_rect_parts[0])

    description_text_parts.append(get_font(Button_config.DESCRIPTION_FONT_SIZE).render(
                        "- No drop from enemies", True, "#605b00"))
    description_rect_parts.append(description_text_parts[1].get_rect(center=(650, 550)))
    Button_config.SCREEN.blit(description_text_parts[1], description_rect_parts[1])

    description_text_parts.append(get_font(Button_config.DESCRIPTION_FONT_SIZE).render(
                        "  - Additional lives are absent", True, "#605b00"))
    description_rect_parts.append(description_text_parts[2].get_rect(center=(665, 580)))
    Button_config.SCREEN.blit(description_text_parts[2], description_rect_parts[2])

    description_text_parts.append(get_font(Button_config.DESCRIPTION_FONT_SIZE).render(
                        "   - Perfect reaction of", True, "#605b00"))
    description_rect_parts.append(description_text_parts[3].get_rect(center=(630, 610)))
    Button_config.SCREEN.blit(description_text_parts[3], description_rect_parts[3])

    description_text_parts.append(get_font(Button_config.DESCRIPTION_FONT_SIZE).render(
                        "turrets and bullets speed", True, "#605b00"))
    description_rect_parts.append(description_text_parts[4].get_rect(center=(665, 640)))
    Button_config.SCREEN.blit(description_text_parts[4], description_rect_parts[4])

    description_text_parts.append(get_font(Button_config.DESCRIPTION_FONT_SIZE).render(
                        "   - No hope...", True, "#605b00"))
    description_rect_parts.append(description_text_parts[5].get_rect(center=(585, 670)))
    Button_config.SCREEN.blit(description_text_parts[5], description_rect_parts[5])
    insane_difficulty = pygame.image.load("Textures/insane_difficulty_icon.png")
    Button_config.SCREEN.blit(insane_difficulty, (420, 550))


def get_difficulty_description_parts(difficulty_button, Button_config):
    if difficulty_button == 1:
        return get_beginner_difficulty_description_parts(Button_config)
    if difficulty_button == 2:
        return get_medium_difficulty_description_parts(Button_config)
    if difficulty_button == 3:
        return get_hard_difficulty_description_parts(Button_config)
    if difficulty_button == 4:
        return get_insane_difficulty_description_parts(Button_config)

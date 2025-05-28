from gamesystem import delayed_print, status_bar,process,battleUI,deathUI
def combat(player,enemy):
    while enemy.health_point > 0:
        if player.health_point > 0:
            status_bar(player,enemy)
            x = battleUI.pop_up()
            process(x ,player,enemy)
            if x.lower() == "escape":
                return enemy
        else:
            delayed_print(f"{player.name} has died.")
            process(deathUI.pop_up())
        if enemy.health_point > 0:
            status_bar(player,enemy)
            process(enemy.choose_action(),enemy,player)
        else:
            delayed_print(f"{enemy.name} has died.")

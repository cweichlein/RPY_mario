import sys
import pygame
import block as bl


def check_events(settings, stats, screen, score_board, blocks, mario, fire_balls, mobs):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, mario, fire_balls)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, settings, mario)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            '''check_play_button(settings, screen, stats, scoreboard, mouse_x, mouse_y, play_button, blocks, mario, 
            fire_balls, mobs)
            check_mode_button(settings, stats, mouse_x, mouse_y, mode_button)'''


def check_keydown_events(event, settings, screen, mario, fire_balls):
    if event.key == pygame.K_SPACE:
        mario.k_space = True
        mario.k_space_held = True
    if event.key == pygame.K_RIGHT:
        mario.change_speed(1, 0)
    elif event.key == pygame.K_LEFT:  # can use elif as each event is only connected to only one key
        mario.change_speed(-1, 0)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, settings, mario):
    if event.key == pygame.K_RIGHT:
        mario.change_speed(-1, 0)
    elif event.key == pygame.K_SPACE:
        mario.k_space_held = False
        mario.k_space = False
    elif event.key == pygame.K_LEFT:  # can use elif as each event is only connected to one key
        mario.change_speed(1, 0)


def create_block(type_set, settings, screen, x, y, blocks):
    new_block = bl.Block(settings, screen)
    new_block_width = new_block.rect.width
    new_block.x = x
    new_block.rect.x = new_block.x
    new_block.y = y
    new_block.rect.y = new_block.y
    blocks.add(new_block)


def create_level(level, settings, screen, blocks, mario, enemies):
    if level == 1:
        dummy_block = bl.Block(settings, screen)
        type_set = 1
        leny = settings.screen_height - dummy_block.rect.height
        lenx = 0
        create_block(type_set, settings, screen, int(settings.screen_width / 2), int(settings.screen_width / 2), blocks)
        while lenx <= settings.screen_width:
            create_block(type_set, settings, screen, lenx, leny, blocks)
            lenx += 32
        create_block(type_set, settings, screen, settings.screen_width - 64, mario.rect.centery, blocks)
        mario.rect.centery = settings.screen_height/2
        mario.rect.centerx = settings.screen_width/2


def fire_ball(settings, screen, mario):
    pass


def throw_fire_ball(settings, screen, mario, fire_balls):
    '''if len(fire_balls) < settings.fire_balls_allowed:
        new_fire_ball = Fire_ball(settings, screen, mario)  # Fire_ball() is from file fire_ball.py
        fire_balls.add(new_fire_ball)'''
    pass


def update_fire_balls(settings, stats, screen, score_board, blocks, mario, fire_balls, mobs):
    '''fire_balls.update()  # move bullets
    for ball in fire_balls.copy():  # remove bullets as they fly off screen
        if ball.rect.bottom <= 0:
            fire_balls.remove(fire_ball)
    # check_bullet_mob_collisions(settings, stats, screen, scoreboard, blocks, mario, fire_balls, mobs)'''
    pass


def update_mobs(settings, stats, screen, mario, mobs):
    '''mobs.update()
    # look for mob-mario collisions
    if pygame.sprite.spritecollideany(mario, mobs):
        mario_hit(stats, mario)
    # check_mobs_bottom(stats, screen, mario, mobs)  # if a mob falls off screen'''
    pass


def update_screen(settings, stats, screen, score_board, blocks, mario, fire_balls, mobs):
    # redraw screen with color each loop pass
    if mario.respawn:
        mario.respawn = False
        # reset(ai_settings, stats, screen, sb, ship, bullets, aliens, alien_bullets, bunkers, bonus, explosions)
    screen.fill(settings.bg_color)
    '''for ball in fire_balls.sprites():
        ball.draw_fire_ball()'''
    mario.blitme()
    # mobs.draw(screen)
    blocks.draw(screen)
    # score_board.show_score()

    # NOTE to team-members of RPY:  THE SECTION BELOW IS FOR WHEN WE IMPLEMENT PLAY BUTTONS.
    # we will pass play button objects as parameters for this function, and will analyze them.
    # SAVE THIS FOR FUTURE. In the mean time, most its content will be commented out.
    # Draw the play button if the game is inactive.
    '''if not stats.game_active:
        score_board.display_main_menu()
        play_button.draw_button()
        mode_button.draw_button()
        if settings.mode == 1:  # display black rect with words that give scores
            score_board.display_high_scores()
        if stats.broke_high_score:
            save_high_score(stats, sb)
            stats.broke_high_score = False'''
    pygame.display.flip()  # Make recent screen visible, by flipping it over the old one

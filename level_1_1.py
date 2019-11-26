from block import *
from settings import Settings
from game_functions import create_block

class level_1_1:
    def __init__(self, setting: Settings, disp: display):
        self.disp = disp

        self.super_list = list()
        self.questions = list()
        self.questions.append(questions(setting,Vector2(17,10), Vector2(1, 1), disp))
        self.questions.append(questions(setting, Vector2(23, 10), Vector2(1, 1), disp))
        self.questions.append(questions(setting, Vector2(25, 10), Vector2(1, 1), disp))
        self.questions.append(questions(setting, Vector2(24, 6), Vector2(1, 1), disp))
        self.questions.append(questions(setting, Vector2(77, 10), Vector2(1, 1), disp))
        self.questions.append(questions(setting, Vector2(93, 6), Vector2(1, 1), disp))
        self.questions.append(questions(setting, Vector2(105, 10), Vector2(1, 1), disp))
        self.questions.append(questions(setting, Vector2(108, 10), Vector2(1, 1), disp))
        self.questions.append(questions(setting, Vector2(111, 10), Vector2(1, 1), disp))
        self.questions.append(questions(setting, Vector2(108, 6), Vector2(1, 1), disp))
        self.questions.append(questions(setting, Vector2(127, 6), Vector2(1, 1), disp))
        self.questions.append(questions(setting, Vector2(128, 6), Vector2(1, 1), disp))

        self.bricks = list()
        self.bricks.append(bricks(setting, Vector2(22, 10), Vector2(1, 1), disp, 'gold'))
        self.bricks.append(bricks(setting, Vector2(24, 10), Vector2(1, 1), disp, 'gold'))
        self.bricks.append(bricks(setting, Vector2(26, 10), Vector2(1, 1), disp, 'gold'))
        self.bricks.append(bricks(setting, Vector2(76, 10), Vector2(1, 1), disp, 'gold'))
        self.bricks.append(bricks(setting, Vector2(78, 10), Vector2(1, 1), disp, 'gold'))
        self.bricks.append(bricks(setting, Vector2(79, 6), Vector2(8, 1), disp, 'gold'))
        self.bricks.append(bricks(setting, Vector2(90, 6), Vector2(3, 1), disp, 'gold'))
        self.bricks.append(bricks(setting, Vector2(93, 10), Vector2(1, 1), disp, 'gold'))
        self.bricks.append(bricks(setting, Vector2(99, 10), Vector2(2, 1), disp, 'gold'))
        self.bricks.append(bricks(setting, Vector2(116, 10), Vector2(1, 1), disp, 'gold'))
        self.bricks.append(bricks(setting, Vector2(119, 6), Vector2(3, 1), disp, 'gold'))
        self.bricks.append(bricks(setting, Vector2(126, 6), Vector2(1, 1), disp, 'gold'))
        self.bricks.append(bricks(setting, Vector2(127, 10), Vector2(2, 1), disp, 'gold'))
        self.bricks.append(bricks(setting, Vector2(129, 6), Vector2(1, 1), disp, 'gold'))

        self.invincibles = list()
        self.invincibles.append(invincible_blocks(setting, Vector2(132, 13), Vector2(1, 1), disp))
        self.invincibles.append(invincible_blocks(setting, Vector2(133, 12), Vector2(1, 2), disp))
        self.invincibles.append(invincible_blocks(setting, Vector2(134, 11), Vector2(1, 3), disp))
        self.invincibles.append(invincible_blocks(setting, Vector2(135, 10), Vector2(1, 4), disp))

        self.invincibles.append(invincible_blocks(setting, Vector2(138, 10), Vector2(1, 4), disp))
        self.invincibles.append(invincible_blocks(setting, Vector2(139, 11), Vector2(1, 3), disp))
        self.invincibles.append(invincible_blocks(setting, Vector2(140, 12), Vector2(1, 2), disp))
        self.invincibles.append(invincible_blocks(setting, Vector2(141, 13), Vector2(1, 1), disp))

        self.invincibles.append(invincible_blocks(setting, Vector2(146, 13), Vector2(1, 1), disp))
        self.invincibles.append(invincible_blocks(setting, Vector2(147, 12), Vector2(1, 2), disp))
        self.invincibles.append(invincible_blocks(setting, Vector2(148, 11), Vector2(1, 3), disp))
        self.invincibles.append(invincible_blocks(setting, Vector2(149, 10), Vector2(1, 4), disp))
        self.invincibles.append(invincible_blocks(setting, Vector2(150, 10), Vector2(1, 4), disp))

        self.invincibles.append(invincible_blocks(setting, Vector2(153, 10), Vector2(1, 4), disp))
        self.invincibles.append(invincible_blocks(setting, Vector2(154, 11), Vector2(1, 3), disp))
        self.invincibles.append(invincible_blocks(setting, Vector2(155, 12), Vector2(1, 2), disp))
        self.invincibles.append(invincible_blocks(setting, Vector2(156, 13), Vector2(1, 1), disp))

        self.invincibles.append(invincible_blocks(setting, Vector2(180, 13), Vector2(1, 1), disp))
        self.invincibles.append(invincible_blocks(setting, Vector2(181, 12), Vector2(1, 2), disp))
        self.invincibles.append(invincible_blocks(setting, Vector2(182, 11), Vector2(1, 3), disp))
        self.invincibles.append(invincible_blocks(setting, Vector2(183, 10), Vector2(1, 4), disp))
        self.invincibles.append(invincible_blocks(setting, Vector2(184, 9), Vector2(1, 5), disp))
        self.invincibles.append(invincible_blocks(setting, Vector2(185, 8), Vector2(1, 6), disp))
        self.invincibles.append(invincible_blocks(setting, Vector2(186, 7), Vector2(1, 7), disp))
        self.invincibles.append(invincible_blocks(setting, Vector2(187, 6), Vector2(1, 8), disp))
        self.invincibles.append(invincible_blocks(setting, Vector2(188, 6), Vector2(1, 8), disp))


        self.floors = list()
        self.floors.append(floor_blocks(setting, Vector2(0, 14), Vector2(68, 2), disp))
        self.floors.append(floor_blocks(setting, Vector2(70, 14), Vector2(15, 2), disp))
        self.floors.append(floor_blocks(setting, Vector2(88, 14), Vector2(63, 2), disp))
        self.floors.append(floor_blocks(setting, Vector2(153, 14), Vector2(64, 2), disp))

        self.pipes = list()
        self.pipes.append(pipe(setting, Vector2(29, 12), Vector2(2, 2), disp, True, True, False))
        self.pipes.append(pipe(setting, Vector2(39, 11), Vector2(2, 3), disp, True, True, False))
        self.pipes.append(pipe(setting, Vector2(47, 10), Vector2(2, 4), disp, True, True, False))
        self.pipes.append(pipe(setting, Vector2(58, 10), Vector2(2, 4), disp, True, True, False))
        self.pipes.append(pipe(setting, Vector2(161, 12), Vector2(2, 2), disp, True, True, False))
        self.pipes.append(pipe(setting, Vector2(177, 12), Vector2(2, 2), disp, True, True, False))

        self.castle = castle(setting, Vector2(201, 13), disp)
        self.flag = flag(setting, Vector2(197, 6), disp)

    def get_rect(self):
        x = list()
        for mybrick in self.bricks:
            x.append(mybrick.get_rect())
        for floor in self.floors:
            x.append(floor.get_rect())
        for pipe in self.pipes:
            x.append(pipe.get_rect())
        for quest in self.questions:
            x.append(quest.get_rect())
        for invinc in self.invincibles:
            x.append(invinc.get_rect())
        x.append(self.flag.get_rect())
        return x

    def draw(self):
        self.disp.fill(Color('#6b8cff'))
        self.castle.draw()
        for brick in self.bricks:
            brick.draw()
        for floor in self.floors:
            floor.draw()
        for quest in self.questions:
            quest.draw()
        for pipe in self.pipes:
            pipe.draw()
        for invinc in self.invincibles:
            invinc.draw()
        self.flag.draw()

    def move(self, velocity, delta):
        for brick in self.bricks:
            brick.move(velocity, delta)
        for floor in self.floors:
            floor.move(velocity, delta)
        for quest in self.questions:
            quest.move(velocity, delta)
        for pipe in self.pipes:
            pipe.move(velocity, delta)
        for invinc in self.invincibles:
            invinc.move(velocity, delta)
        self.flag.move(velocity, delta)
        self.castle.move(velocity, delta)
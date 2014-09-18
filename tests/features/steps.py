# -*- coding: utf-8 -*-
from lettuce import *
import app.match as m


@step(u'Given: "([^"]*)" and "([^"]*)" start a match to "([^"]*)" sets')
def given_group1_and_group2_start_a_match_to_group3_sets(step, player1, player2, sets):
    world.match = m.Match(player1, player2, sets)

@step(u'Then: I see score: "([^"]*)"')
def then_i_see_score_group1(step, score):
    assert world.match.score_set() == score, \
        "Got %s" % world.match.score_set()


@step(u'When: "([^"]*)" won the "([^"]*)" set "([^"]*)"-"([^"]*)"')
def when_group1_won_the_group2_set_group3_group4(step, player1, numset, ptoPlayer1, ptoPlayer2):
    world.match.save_set_won(player1)
    world.match.save_score_set(ptoPlayer1, ptoPlayer2, numset, player1)


@step(u'And: "([^"]*)" won the "([^"]*)" set "([^"]*)"-"([^"]*)"')
def and_group1_won_the_group2_set_group3_group4(step, player1, numset, ptoPlayer1, ptoPlayer2):
    world.match.save_set_won(player1)
    world.match.save_score_set(ptoPlayer1, ptoPlayer2, numset, player1)


@step(u'Then: The match score is: "([^"]*)"')
def then_the_match_score_is_group1(step, score):
    assert world.match.score_set() == score, \
        "Got %s" % world.match.score_set()

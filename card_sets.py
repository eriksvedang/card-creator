
# all sizes are in cm

main_set = {
	'name': "MainSet",
	'margin': 1.0, # from the top and left of the page
	'spacing': 0.02, # between the cards
	'card_size': (6.3, 8.8), # the size (including the border) of each card
	'border_width': 0.25, # at the edge of each card
	'border_color': (150, 150, 150),
	'cards_per_page': 9,
	'cards': [
			{'name': "Big Time", 			'illustration': "big_time", 'body': "Gain 3 points.", 'body_width': 25, 'corner_nr': "0", 'count': 4, }, 
			{'name': "Destruction", 		'illustration': "destruction", 'body': "Trash a card.", 'body_width': 25, 'corner_nr': "0", 'count': 3, },
			{'name': "Ambush!", 			'illustration': "ambush", 'body': "Put a card from your hand into play face up.", 'body_width': 23, 'corner_nr': "2", 'count': 3},
			{'name': "Hecatomb", 			'illustration': "hecatomb", 'body': "Trash any number of cards you control to gain that many points.", 'body_width': 24, 'corner_nr': "2", 'count': 3},
			{'name': "Simplicity", 			'illustration': "simplicity", 'body': "Gain 1 point.", 'body_width': 25, 'corner_nr': "4", 'count': 3},
			
			{'name': "Catch Up", 			'illustration': "catch_up", 'body': "The player with the least points (if any) gains 5 points.", 'body_width': 24, 'corner_nr': "2", 'count': 3},
			{'name': "Time Machine", 		'illustration': "time_machine", 'body': "Lose 5 points. You can use two additional cards this turn.", 'body_width': 25, 'corner_nr': "1", 'count': 3},
			{'name': "Together We Fall", 	'illustration': "together_we_fall", 'body': "Both players lose 7 points.", 'body_width': 35, 'corner_nr': "1", 'count': 3},
			{'name': "Scoundrels", 			'illustration': "scoundrels", 'body': "Both players may play up to two cheats from their hands.", 'body_width': 23, 'corner_nr': "3", 'count': 3},
			{'name': "Rescue Mission", 		'illustration': "rescue_mission", 'body': "Lose 2 points. Pick a trashed card and put it into play (unused).", 'body_width': 25, 'corner_nr': "1", 'count': 3},
			
			{'name': "Working 9 to 5", 		'illustration': "working_9_to_5", 'body': "Gain 2 points.", 'body_width': 25, 'corner_nr': "2", 'count': 3},
			{'name': "Late Bloomer", 		'illustration': "late_bloomer", 'body': "Gain 1 point. Turn a card into a cheat.", 'body_width': 25, 'corner_nr': "1", 'count': 3},
			{'name': "Metamorphic", 		'illustration': "metamorphic", 'body': "Gain 1 point. Flip up a cheat.", 'body_width': 17, 'corner_nr': "2", 'count': 3},
			{'name': "Duplicate", 			'illustration': "duplicate", 'body': "Both players double their points.", 'body_width': 20, 'corner_nr': "2", 'count': 3},
			{'name': "The Sublime", 		'illustration': "the_sublime", 'body': "Trash this card. Make two used cards usable again.", 'body_width': 20, 'corner_nr': "1", 'count': 3},
			
			{'name': "Destiny", 			'illustration': "destiny", 'body': "Put the top card of the deck into play.", 'body_width': 20, 'corner_nr': "3", 'count': 3},
			{'name': "Philantropist", 		'illustration': "philantropist", 'body': "Make one of your cards usable and give it to your opponent.", 'body_width': 21, 'corner_nr': "4", 'count': 3},
			{'name': "Anarchy", 			'illustration': "anarchy", 'body': "Each player gains 1 point for each cheat they have in play. Trash all cheats.", 'body_width': 28, 'corner_nr': "2", 'count': 3},
			{'name': "Ancient Riches", 		'illustration': "pyramid", 'body': "Gain 1 point for each card in the trash pile.", 'body_width': 25, 'corner_nr': "1", 'count': 3},
			{'name': "Peddler", 			'illustration': "peddler", 'body': "Trash an unused card you control. Gain points equal to that card's star power.", 'body_width': 30, 'corner_nr': "1", 'count': 3},
			
			{'name': "Silence", 			'illustration': "silence", 'body': "Until the end of your next turn, players cannot gain points.", 'body_width': 22, 'corner_nr': "3", 'count': 3},
			{'name': "Purge", 				'illustration': "purge", 'body': "Gain 1 point. Trash all used cards.", 'body_width': 22, 'corner_nr': "1", 'count': 3},
			{'name': "Late to the Party", 	'illustration': "neon", 'body': "The player with the lowest total star power (if any) gains 4 points.", 'body_width': 25, 'corner_nr': "2", 'count': 3},
			{'name': "Faster than the Eye", 'illustration': "hands", 'body': "Turn any number of cards you control into cheats.", 'body_width': 25, 'corner_nr': "2", 'count': 3},
	],
}
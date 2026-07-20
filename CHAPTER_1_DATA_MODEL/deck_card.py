import collections

# Card = collections.namedtuple('Card',['rank','suit'])

# c = Card('1','spade')
# print(c[0])

            # question 1
# 1. Create a namedtuple called Point with fields x and y. Create an 
# instance p = Point(3, 4).
#  Predict, then verify: what does print(p) output?

# Point = collections.namedtuple('Point',['x','y'])
# p = Point(3,4)
# print(p)

# 2. Using that same p, what do p[0] and p[1] give you? 
# Why do both of those work even though you never wrote 
# a __getitem__ method yourself?
# print(p[0])
# print(p[1]) # we dont need to write the --getitem for ourself as the namedtuple is the
            # subclass of the tuple were positional indexing exists through __getitem__


# 3. Create two separate Point instances with the same x and y values,
#  e.g. p1 = Point(1, 2) and p2 = Point(1, 2). Predict: does p1 == p2 
#  return True or False? Then run it and check. 
# (Hint: think about what dunder method == routes through, and whether
#   namedtuple gives you that for free too.)

# p1 = Point(1,2)
# p2 = Point(1,2)
# print(p1 == p2) # as tuple class has __eq__ so that the namedtuple would also inherit this


""" Question 2 """

# 4. Create a namedtuple called Card3D with fields suit, 
# rank, and deck_id. Then write a plain Python list containing
# 5 different Card3D instances. Without writing any custom code,
# try calling len() on that list, and try accessing the 3rd card with [2]. 
# Then explain in your own words: is the len()/[ ] 
# behavior here coming from Card3D, or from the list? Why does that distinction matter?

# Card3D = collections.namedtuple('Card3D',['suit','rank','deckid'])

# card_instances = [Card3D('spade',3,'01'), Card3D('diamond',4,'02'), Card3D('king',5,'03')]
# print(len(card_instances))
# print(card_instances[2])

# these behaviours are coming from list 


""" Question 3 """

# 5. Without using namedtuple, hand-write a plain class called ManualCard 
#     with __init__(self, rank, suit) that stores rank and suit. 
#     Create an instance and print() it. Compare that output to what
#     namedtuple's Card gave you earlier. Then add a __repr__ method '
#     'to ManualCard yourself so that printing it looks like '
#     'ManualCard(rank='7', suit='diamonds') — matching what namedtuple '
#     'gave you automatically.'
# ' This one's meant to make you feel what namedtuple was doing for you
# behind the scenes.

# class ManualCard:
#     """Models the cards deck"""
#     def __init__(self,rank,suit):
#         """Initialized the rank and suit"""
#         self.rank = rank
#         self.suit = suit
    
#     def __repr__(self):
#         return f"ManualCard(Rank={self.rank!r}, Suit={self.suit!r})"
    

# mc = ManualCard('4','spades')
# print(mc)


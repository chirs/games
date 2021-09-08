



def express():

    # make all possible picks of best player by position you don't have.
    # how do you know what's the right result?
    

    players = [
        (100, 50, 0),
        (100, 25, 0),
        (75, 50, 0),
        ]

    # just my guess
    order = [
        'mccaffrey', # 300 rb
        'mahomes', # 400 qb

        'adams', # 250 wr
        'allen', # 350 qb

        'hill', # 225 wr
        'diggs', # 175 wr
        'murray', # 300 qb
        'cook', # 225 rb
        'henry' # 200 rb
        ]

    # pretty sure #3 ends up with adams, allen, and henry
    # so if #1 picks mahomes, they end up with mahomes, ..., ...
    # and #2 ends up with mccaffrey, ..., ...


    # first 4 picks are mahomes, mccaffrey, adams, allen


    # 1: 300 + 175 + 300 = 775
    # 2: 400 + 225 + 225 = 850
    # 3: 250 + 350 + 200 = 800

    # second guess

    # a mahomes
    # b mccaffrey
    # c adams
    # c allen
    # b hill
    # a cook
    # a diggs
    # b murray
    # c henry


    # 1: 400 + 225 + 175 = 800
    # 2: 300 + 225 + 300 = 825
    # 3: 250 + 350 + 200 = 800


    
    
        

# obliquelaw. A project to give constraints to legal analysts to promote creative outcomes and avoid writer's block.  Inspired by Brian Enos's Oblique Strategies

import random


strategies = [
    'What would the dissenting opinion say about it?',
    'Make your argument using only pictures and diagrams.',
    'What\'s the second best policy argument to make on this point?',
    'How would Atticus Finch argue this point?',
    'Assume you lost. Why\'d it happen & how should you have stopped it?',
    'If the law did not exist, how should this be decided?',
]

if __name__ == '__main__':
    strategy = random.choice(strategies)
    print(strategy)

#figure out how to put online using django or flask
#figure out how to show it in nicer font
#figure out how to change background colors
#figure out how to allow people to choose another

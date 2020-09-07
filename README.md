# Monopoly-stats
A short python program to analyse probability in monopoly

There are 2 modes
1. probabilty of landing on specific squares
2. probabilty of rolling a specific number

The python script allows monopoly to be played by 1 virtual token for and record where it lands over 100,000,000 moves. This then shows the most common tiles to land on and is able to use te purchase price of each property to show the estimated value of each tile.

A few factors influence the probility of landing on a particular square, some of these are

- The probabilty of the total of time dice rolls (a good website to show this visually is [any dice](https://anydice.com)
- Chance and community chest cards which say to go to a specific tile
- Distance to the "jail', since 2 tiles ("jail" and "go to jail") effectivly make you end your turn on the same tile and since a few community chest cards nd chance cards send the player to jail, jail is by far the most likely square to land on, therefor some tiles are more likely to be landed on since they are about 7 tiles away from jail

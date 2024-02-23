# Pokemaster

## First 'Mini' Game

- Command line type effectiveness
- Query the API for 2 types - designate 1 as the Defensive type - designate 1 as the Attack type - User will input 1, 2, 3, or 4 for type effectivenesss of Attacker vs Defender
  1. 0x effective
  2. 0.5x effective
  3. 1x effective
  4. 2x effective
     \*\*Note: this is only considering single type combinations

## Games

1. **Type Effectiveness Game**

   - Upon start, display a random type as well as a list of all 18 types. - Users can drag and drop from the list of types into 4 different categories (2x, 1x, 0.5x, 0x) based on the effectiveness when attacking the focal type. \* if Fire was the focal type, the user would be correct to move Water to the 2x category. - After submitting their answers, users will see feedback for which types they correctly identified the effectiveness for. - User will be prompted to continue or exit.

2. **Advanced Type Effectiveness Game**

   - Same concept as the Type Effectiveness Game, but users will be prompted with dual types. - This game should only display legitimate type pairings that exist on Pokemon. - This may add additional effectiveness categories

3. **Pokemon Type Guessing Game**
   - Users will be shown a random Pokemon and a list of all 18 types.
   - Users need to selected up to 2 types that they believe the Pokemon to be.
   - User will be receive feedback and prompted to continue or exit.
4. **Pokedex Guesser**
   - User will try to input all pokemon in a generation

## Info

1.  **Type Description Page**
    - Individual Pages for each Type with 4 lists (2x, 1x, 0.5x, 0x) of corresponding types effectivenesses
    - 2 lists for Primary and Secondary typing, that contain pokemon with that typing.
2.  **Pokemon Description Page**
    - Individual Page for Pokemon with their type and effectivenesses to them
    - Available moves that can learned
    - Base stats

## Builder

1.  **Pokemon Builder**

    - Ability to pick a pokemon, their moves, IVs, and EVs.
    - Can build a game around this where this pokemon is matched against a random pokemon, and user has to determine effectiveness of their pokemon's moves.
      - could have an easy and hard mode. Easy mode would give the random pokemon's typing, hard would not give the pokemon's typing.
      - extra super hard mode - do something with atk/def sp atk/ sp def

2.  **Team Builder**

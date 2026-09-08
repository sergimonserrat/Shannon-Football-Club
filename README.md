# Shannon-Football-Club
A coding project looking for the most 'unpredictable' teams in LaLiga.

This was an attempt to measure the unpredictability of teams in LaLiga (1928-29 to 2023-24). It treats the W-D-L record of a team in any given season as a probability distribution. It was first designed to find the highest Shannon entropy, which favoured teams with an equal share of wins, draws and losses. Although unpredictable, I was not satisfied with the answer. Mid table clubs with lots of draws did not fit my preconceived notion of "unpredictability = excitement". That is why I opted to use 50%-0%-50% as a reference distribution. This way I was targetting teams that either win or lose in equal amounts and that rarely draw. The Jensen-Shannon distance was most appropriate for this task.

## Repository structure
- `Calcul_Shannon_futbol.py`: main code
- `historic.pkl`: historical football data.

| Column | Type | Description |
|---|---|---|
| Pos. | integer | Position in the league table |
| Team | string | Name of the club |
| Pts. | string | Points. Although integer in nature, it includes anotations (e.g.: 42**, 33#...) |
| W | integer | wins |
| D | integer | Draws |
| L | integer | Losses |
| F | integer | Goals for |
| A | integer | Goals against |
| YC | integer | Yellow cards |
| RD | integer | Red cards |
| Temp | string | Season (e.g.: 1928-29) |

- `Scrape_Shannon_futbol.py`: script originally used to scrape the data from the website bdfutbol.com. It is unlikely to work since the code was only used once and websites modify their html code frequently enough as to have fallen out of date by now. It was also coded with chromedriver in mind. It is attached here for the sake of completeness.

## Code description

- Columns are added to express W-D-L as fractions of total matches instead of whole numbers.
- Logarithm in base 3 is taken so the Shannon entropy falls in the [0, 1] interval.
- A column H is created where the Shannon entropy for each teams and season is computed.
- Aggregate dataframes `Prova`, `Maxims` and `Equips` are created with 3 relevant columns: Temp (season), Team, and Entropia (entropy).
- The same process is repeated to compute the Jensen-Shannon distance, which is stored in the column JSD.
- The top 10 teams with the lowest distance are printed on screen.

The code does not save the aggregate dataframes. They can be easily explored using spdyer as your IDE.

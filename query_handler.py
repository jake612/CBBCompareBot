from google.cloud import bigquery
client = bigquery.Client()

# Given two players, return head to head matchups and stats
def compare_players(player1, player2):
    # Note: I'm aware of the security vulnerabilities and general problems of taking in string values to format SQL queries
    # For now, I'm going to get the application working, then focus on rectifying the issue
    query = ("""SELECT P1.points AS p1points, P2.points AS p2points
FROM `bigquery-public-data.ncaa_basketball.mbb_players_games_sr` P1, `bigquery-public-data.ncaa_basketball.mbb_players_games_sr` P2
WHERE P1.full_name="{}" AND P2.full_name="{}" AND P1.game_id=P2.game_id""".format(player1, player2)
             )

    query_job = client.query(query, location="US",)

    results = query_job.result()
    for row in results:
        print(row)




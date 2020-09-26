#Uses key terms extracted by whichRequest to
# - build query
# - request from bigQuery database
# - return the result to be handled by interpretQUery

from google.cloud import bigquery

def stateQuery(state) :

    client = bigquery.Client.from_service_account_json("ShellHacks2020-487e58d8d077.json")
    query_job = client.query(
        """
        SELECT *
        FROM `bigquery-public-data.covid19_public_forecasts.state_14d`
        WHERE state_name = """ + state

    )
    print("The query data:")
    for row in query_job:
        # Row values can be accessed by field name or index.
        print("name={}, count={}".format(row[0], row["total_people"]))
    return()


# def countyQuery(county, state) :
#     client = bigquery.Client.from_service_account_json(ShellHacks2020-487e58d8d077.json)
#     query_job = client.query(
#         """
#         SELECT *
#         FROM `bigquery-public-data.covid19_public_forecasts.state_14d`
#         WHERE state_name = @state
#         """
#     )
#     return(query_job)

stateQuery("Texas")
#Uses key terms extracted by whichRequest to
# - build query
# - request from bigQuery database
# - return the result to be handled by interpretQUery

from google.cloud import bigquery

def stateQuery(statecode) :

    client = bigquery.Client.from_service_account_json("ShellHacks2020-487e58d8d077.json")

    #Parameterized Query
    query = '''
        SELECT *
        FROM `bigquery-public-data.covid19_public_forecasts.state_14d`
        WHERE state_fips_code = @state_fips_code 
            AND prediction_date >= forecast_date
        ORDER BY prediction_date
    '''
    job_config = bigquery.QueryJobConfig(
        query_paramters=[
            bigquery.ScalarQueryParameter("state_fips_code", "INT64", statecode)
        ]
    )
    query_job = client.query(query, job_config=job_config)

    for row in query_job:
        # Row values can be accessed by field name or index.
        print("name={}, count={}".format(row[0], row["new_deaths"]))
    return()

stateQuery(48)
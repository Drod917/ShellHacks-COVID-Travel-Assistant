from google.cloud import bigquery


def query(cleaned_query):
    client = bigquery.Client()
    query_job = client.query(cleaned_query)  # API request
    rows = query_job.result()  # Waits for query to finish

    dirty = []
    # Iterate through result
    for row in rows:
        dirty.append(row)
    clean = []
    for row in dirty:
        clean.append(dict(row))
    return clean
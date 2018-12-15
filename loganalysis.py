#! /usr/bin/env python3
import psycopg2
DBNAME = "news"
# connect to the news database
try:
 db = psycopg2.connect(database=DBNAME)
except psycopg2.DatabaseError, e:
 print("<error message>")
# method to execute the queries and return the result


def execute_query(query):
    c = db.cursor()
    c.execute(query)
    rows = c.fetchall()
    return rows


def print_query(query):
    for row in query:
     print("\"" + str(row[0]) + "\"" + '-' + str(row[1]) + 'views')
     print("\n")
# -------------------------------Q1
first_query = """SELECT title, count(*) AS views
  FROM articles, log
  WHERE log.status = '200 OK'
     AND log.path = '/article/' || articles.slug
  GROUP BY articles.title
  ORDER BY views DESC
  LIMIT 3;
  """
# print the result query
first_result = execute_query(first_query)
print('Query 1:What are the most popular three articles of all time?')
print_query(first_result)

# -------------------------------Q2
second_query = """SELECT name, count(*) as views
  FROM articles, authors, log
  WHERE log.path = '/article/' || articles.slug
    AND articles.author = authors.id
  GROUP BY authors.name
  ORDER BY views DESC;
  """
# print the result query
second_result = execute_query(second_query)
print('Query 2: Who are the most popular article authors of all time?')
print_query(first_result)

# -------------------------------Q3

third_query = """SELECT TO_CHAR(count.day, 'FMMonth DD, YYYY'),
    ROUND((( errors.errored_requestes*1.0 ) / count.requests ), 3)
    AS percent
    FROM (SELECT date_trunc('day', time) "day", count(*) AS errored_requestes
    FROM log WHERE status != '200 OK'
    GROUP BY day) AS errors
        JOIN (
          SELECT date_trunc('day', time) "day", count(*) AS requests
          FROM log
          GROUP BY day) AS count
        ON count.day = errors.day
        WHERE (ROUND(((errors.errored_requestes*1.0) / count.requests), 3) > 0.01)
        ORDER BY percent DESC;
    """
# print the result query
third_result = execute_query(third_query)
print('Query 3: Days on which more than 1% of requests lead to errors?')
# to change the date format
for row in third_result:
  for date, error in third_result:
    print(date + '-' + str(round(error*100, 1)) + "%")
db.close()

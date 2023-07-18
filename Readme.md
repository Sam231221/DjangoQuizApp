QuizApp with ClientSideTimer
NO Connection to Heorku Database
AWS S3 Bucket Used.
You need dj_database_url for the Postgres Database to run in production environment.
Otherwise you will receive error like this:
connection to server at "localhost" (127.0.0.1), port 5432 failed: Connection refused
Is the server running on that host and accepting TCP/IP connections?

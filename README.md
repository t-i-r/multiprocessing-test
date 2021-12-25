### Dash app: Test connection to postgres from a separate process. 
2021-12-25

- Need to change
2020-06-08

- The goal is to be able to run long running function in a separete process but still be able to write results to database opened in the main app
- Simple dash app for testing of database connection that was opened in dash main app, can be used in a separate processs
- Check if it is possible to read/write to postgres with from separate process.
- Requires postgres with person table (e.g. running as docker container) accessed via [peewee](http:\\peewee) ORM

Modifying this file is simple

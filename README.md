# Dijkstra_psycopg2

## Dijkstra's Algorithm
the algorithm is a solution to the single-source shortest path problem in graph theory.

works on both directed and undirected graphs. but, all edges must have nonnegative weights.


\
In my code, it can be divided into two.

#### Preparing
1. connect db
2. initialize
    - prepare start, end node
    - count nodes in db
    - init distances' weight (40000 instance of infinite)
#### Dijkstra
repeat until found all nodes' shortest path or node' shortest path we're looking for
1. pick vertex in list with minimum distance
2. find and save vertex's neighbors informations(id, weight)
3. update neighbors' weight and route if they are less than previously computed

## psycopg2 (for using postgreSQL in python)
```python
import psycopg2 as pg2

db = pg2.connect(host='address', dbname='database's name', user='user name', password='password', port='port number')

db.autocommit = True #PostgreSQL automatically commits, but you have to set up the autocommit separately in Python.
cursor = db.cursor() # declare for command execution.

db.close()
```

create database
```python
cursor.execute('CREATE DATABASE myDatabase')
```

create table
```python
cursor.execute('CREATE TABLE myTable(id INTEGER, date DATE, name VARCHAR(20))')
```

insert value into table
```python
cursor.execute('INSERT INTO myTable VALUES (1, '2022-01-01', 'kim'), (2, '2022-01-02', 'Jay')')
```

look up data
```python
cursor.execute('SELECT * FROM myTable')
cursor.fetchall() # return list type to terminal.
```


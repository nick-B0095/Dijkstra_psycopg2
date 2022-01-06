import psycopg2 as pg2

def select(cursor, colum, table, where = None): # sql query(select)
    if where is None:
        sql = f'SELECT {colum} FROM {table}'
    else:
        sql = f'SELECT {colum} FROM {table} WHERE {where}'
    cursor.execute(sql)
    return cursor.fetchall()

def extractMin(Q, d): # find lowest weight's key in d
    min_key = None
    for v in Q:
        if min_key is None:
            min_key = v
        elif d[min_key] > d[v]:
            min_key = v
    return min_key

db = pg2.connect(host='localhost', dbname='problem', user='postgres', password='121221', port=5432)
db.autocommit=True

cursor=db.cursor()

start = int(input('출발 노드를 입력하세요:'))
end = int(input('도착 노드를 입력하세요:'))

table = 'route'
V=select(cursor, 'count(distinct(sid))', table)[0][0] # the number of Vertices

d = {}
d = [40000 for _ in range(V+1)] # init distance weight
route = {}

d[start] = 0 # start node's weight is 0

prevV = set() # set of vertices
Q = set()
memory_W = {}
init = True


while len(prevV) != V:
    # pick vertex(v) in list with minimum distance.
    if init is True:
        v = start
        prevV.add(v)
        init = False
    else:
        prevV.add(v)
        v = extractMin(Q, d)
        Q.remove(v)
    
    # exit when we reach minimum distance we're looking for
    if v == end:
        break
    
    # find and save v's neighbors info(id, weight)
    q=[]
    for x in select(cursor, 'fid, weight', table, f'sid={v}'): # vertex connected from v
        q.append(x[0]) # v's neighbors id list
        memory_W[f'{v}, {x[0]}'] = x[1] # v's neighbors weight list
    
    # if the neighbor has already been picked as v, exclude from neighbors list
    Q.update(q)
    Q = Q - prevV

    # update neighbors' weight if it is less than previously computed
    for neighbor in Q:
        try:
            w = memory_W[f'{v}, {neighbor}']
            if (d[v] + w < d[neighbor]): # is it less than previously computed? Y
                d[neighbor] = d[v] + w # update neighbor's minimum wieght
                try:
                    route[neighbor] = f'{route[v]}, {v}' # update neighbor's route about minmum distance
                except KeyError: #route[v] is not existed
                    route[neighbor] = f'{v}'


        except KeyError: #(v, neighbor) is not connected
            w = None

print(f'경로는 [{route[end]}, {end}]입니다.')

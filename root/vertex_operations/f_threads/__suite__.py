name = "Threads"
description = "Vertex Query as a function of number of threads."

table_view = [
    [{"sTitle":"Database engine"},{"content":"object.engine()"}],
    [{"sTitle":"Version"},{"content":"object.engine()"}],
    [{"sTitle":"Platform"},{"content":"object.platform()"}],
    [{"sTitle":"Threads"},{"content":"'T:%d'%(object.threads())"}],
    [{"sTitle":"Rate (v/s)"},{"content":"'%.2f'%(object.rate_avg())"}],
    [{"sTitle":"Time (ms)"},{"content":"object.time_avg()"}]
    ]

plot_view = {
    "plot":[
        {"name":"rate","data":("object.rate_avg()","object.threads()"),"xaxis":"Threads"},
        {"name":"memory","data":("object.memory_used_avg()*1e-6","object.threads()"),"xaxis":"Threads"},
        ],
    "ivar":[
        {"name":"Platform","id":"object.platform_id()","content":"object.platform()"},
        {"name":"Version","id":"object.engine_id()","content":"object.engine()"},
        ]
    }

graph_size = pow(2,14)*80
query_size = pow(2,14)*80
tx_size = pow(2,14)
page_size = 14
cases = []
threads = [1,2,3,4,5,6,7,8]

index_case = {
    "name":"ingest",
    "description":"Vertex Ingestion as a function of number of threads. (page size=%d, transaction size=%d)"%(pow(2,page_size),tx_size),
    "type":"vertex_ingest",
    "data":
    {
        "template":["basic"],
        "config":["default:default"],
        "page_size":[14],
        "threads":[1],
        "use_index":[1],
        "new":1,
        "txsize":[tx_size],
        "size":[graph_size],
        "ig_version":["ig.3.0","ig.3.1"]
        },
    "table_view":table_view,
    "plot_view":plot_view
    }
cases.append(index_case)

for thread in threads:    
    query_case = {
        "name":"query",
        "description":"Vertex Query as a function of threads (graph_size=%d,query_size=%d)."%(graph_size,query_size),
        "type":"query",
        "data":
        {
            "template":["basic"],
            "vertex":["Node"],
            "config":["default:default"],
            "page_size":[14],
            "threads":[thread],
            "txsize":[tx_size],
            "txlimit":[10],
            "size":[query_size],
            "graph_size":[graph_size],
            "ig_version":["ig.3.0","ig.3.1"]
            },
        "table_view":table_view,
        "plot_view":plot_view
        }   
    cases.append(query_case)
    pass

    

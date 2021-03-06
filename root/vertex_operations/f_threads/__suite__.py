name = "Threads"
description = "Vertex Query as a function of number of threads."

table_view = [
    [{"sTitle":"Version"},{"content":"object.engine()"}],
    [{"sTitle":"Platform"},{"content":"object.platform()"}],
    [{"sTitle":"Threads"},{"content":"object.threads()"}],
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
        {"name":"Index","id":"object.index_type_id()","content":"object.index_type()"},
        ]
    }

graph_size = pow(2,20)
query_size = pow(2,18)
tx_size = pow(2,14)
page_size = 14
cases = []
threads = [1,2,4,8,16]

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
        "ig_version":["ig.3.2","ig.3.1"]
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
            "use_index":[1],
            "size":[query_size],
            "graph_size":[graph_size],
            "ig_version":["ig.3.2","ig.3.1"]
            },
        "table_view":table_view,
        "plot_view":plot_view
        }   
    cases.append(query_case)
    pass

    
cases = [
    {
    "name":"ingest",
    "description":"Vertex Ingestion as a function of number of threads. (page size=%d, transaction size=%d)"%(pow(2,page_size),tx_size),
    "type":"vertex_ingest",
    "data":
    {
    "template":["basic"],
    "config":["default:default"],
    "page_size":[14],
    "threads":threads,
    "use_index":[0,1],
    "new":1,
    "txsize":[tx_size],
    "size":[graph_size],
    "ig_version":["ig.3.2","ig.3.1"]
    },
    "table_view":table_view,
    "plot_view":plot_view
    }
    ]

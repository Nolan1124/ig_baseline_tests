name = "Threads"
description = "Vertex Ingestion as a function of number of threads."

table_view = [
    [{"sTitle":"Database engine"},{"content":"object.engine()"}],
    [{"sTitle":"Graph Scale"},{"content":"'scale:%d'%(math.log(object.graph_size(),2))"}],
    [{"sTitle":"Threads"},{"content":"'T:%d'%(object.threads())"}],
    [{"sTitle":"Index Type"},{"content":"'index:%s'%(object.index_type())"}],
    [{"sTitle":"Rate (v/s)"},{"content":"'%.2f'%(object.rate_avg())"}],
    [{"sTitle":"Time (ms)"},{"content":"object.time_avg()"}],
    [{"sTitle":"Heap Memory (MB)"},{"content":"'%.3f'%(object.memory_used_avg()*1e-6)"}],
    ]

plot_view = {
    "plot":[
        {"name":"rate","data":("object.rate_avg()","object.threads()"),"xaxis":"Threads"},
        {"name":"memory","data":("object.memory_used_avg()*1e-6","object.threads()"),"xaxis":"Threads"},
        ],
    "ivar":[
        {"name":"Platform","id":"object.platform_id()","content":"object.platform()"},
        {"name":"Index Type","id":"object.index_type_id()","content":"object.index_type()"},
        ]
    }

graph_size = pow(2,18)*40
query_size = pow(2,18)
tx_size = pow(2,14)
page_size = 14
cases = []
threads = [1,2,3,4,5,6,7,8]

for thread in threads:
    no_index_case = {
        "name":"ingest",
        "description":"Vertex Ingestion as a function of number of threads. (page size=%d, transaction size=%d)"%(pow(2,page_size),tx_size),
        "type":"vertex_ingest",
        "data":
        {
            "template":["basic"],
            "config":["default:default"],
            "page_size":[14],
            "threads":[thread],
            "use_index":[0],
            "new":1,
            "size":[graph_size],
            "txsize":[tx_size],
            "ig_version":["ig.3.0"]
            },
        "table_view":table_view,
        "plot_view":plot_view
        }
    cases.append(no_index_case)
    pass

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
        "ig_version":["ig.3.0"]
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
            "size":[query_size],
            "graph_size":[graph_size],
            "ig_version":["ig.3.0"]
            },
        "table_view":table_view,
        "plot_view":plot_view
        }   
    cases.append(query_case)
    pass

threads = threads[1:]
for thread in threads:
    index_case = {
        "name":"ingest",
        "description":"Vertex Ingestion as a function of number of threads. (page size=%d, transaction size=%d)"%(pow(2,page_size),tx_size),
        "type":"vertex_ingest",
        "data":
        {
            "template":["basic"],
            "config":["default:default"],
            "page_size":[14],
            "threads":[thread],
            "use_index":[1],
            "new":1,
            "txsize":[tx_size],
            "size":[graph_size],
            "ig_version":["ig.3.0"]
            },
        "table_view":table_view,
        "plot_view":plot_view
        }
    cases.append(index_case)
    
    

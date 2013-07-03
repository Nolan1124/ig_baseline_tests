name = "Process"
description = "Vertex Query as a function of number of threads."

table_view = [
    [{"sTitle":"Version"},{"content":"object.engine()"}],
    [{"sTitle":"Platform"},{"content":"object.platform()"}],
    [{"sTitle":"Process"},{"content":"'T:%d'%(object.processes())"}],
    [{"sTitle":"Rate (v/s)"},{"content":"'%.2f'%(object.rate_avg())"}],
    [{"sTitle":"Time (ms)"},{"content":"object.time_avg()"}]
    ]

plot_view = {
    "plot":[
        {"name":"rate","data":("object.rate_avg()","object.processes()"),"xaxis":"Processes"},
        {"name":"time","data":("object.time_avg()","object.processes()"),"xaxis":"Processes"},
        ],
    "ivar":[
        {"name":"Platform","id":"object.platform_id()","content":"object.platform()"},
        {"name":"Version","id":"object.engine_id()","content":"object.engine()"},
        {"name":"Index Type","id":"object.index_type_id()","content":"object.index_type()"},
        ]
    }

graph_size = pow(2,18)
query_size = pow(2,12)
tx_size = pow(2,15)
page_size = 14
cases = []
processes = [(None,1),(None,2),(None,3),(None,4),(None,5)]

     
for process in processes:
    cases.append(
        {
            "name":"ingest",
            "description":"Vertex Ingestion as a function of number of threads. (page size=%d, transaction size=%d)"%(pow(2,page_size),tx_size),
            "type":"vertex_ingest",
                "data":
            {
                "template":["basic_non_unique"],
                "config":["default:default"],
                "page_size":[14],
                "threads":[1],
                "use_index":[1],
                "new":1,
                "txsize":[tx_size],
                "size":[graph_size],
                "ig_version":["ig.3.1","ig.3.0"],
                "process":[process],
                },
            "table_view":table_view,
            "plot_view":plot_view
            }
        )
    cases.append(
        {
            "name":"query",
            "description":"Vertex Query as a function of number of processes. (page size=%d, transaction size=%d)"%(pow(2,page_size),tx_size),
            "type":"query",
            "data":
            {
                "template":["basic_non_unique"],
                "vertex":["Node"],
                "config":["default:default"],
                "page_size":[14],
                "threads":[1],
                "use_index":[1],
                "txsize":[tx_size],
                "size":[query_size],
                "graph_size":[graph_size],
                "ig_version":["ig.3.1","ig.3.0"],
                "process":[process],
                },
            "table_view":table_view,
            "plot_view":plot_view
            }
        )
    pass
    
cases.append(
    {
        "name":"ingest",
        "description":"Vertex Ingestion as a function of number of threads. (page size=%d, transaction size=%d)"%(pow(2,page_size),tx_size),
        "type":"vertex_ingest",
        "data":
        {
            "template":["basic_non_unique"],
            "config":["default:default"],
            "page_size":[14],
            "threads":[1],
            "use_index":[0],
            "new":1,
            "txsize":[tx_size],
            "size":[graph_size],
            "ig_version":["ig.3.1","ig.3.0"],
            "process":processes,
            },
        "table_view":table_view,
        "plot_view":plot_view
        }
    )

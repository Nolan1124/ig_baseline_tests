name = "Transaction Size"
description = "Vertex Ingestion as a function of transaction size."

tx_sizes = []
for i in xrange(8,19):
    tx_sizes.append(pow(2,i))
    pass

table_view = [
    [{"sTitle":"Version"},{"content":"object.engine()"}],
    [{"sTitle":"Transaction Size"},{"content":"object.tx_size()"}],
    [{"sTitle":"Index Type"},{"content":"'index:%s'%(object.index_type())"}],
    [{"sTitle":"Rate (v/s)"},{"content":"'%.2f'%(object.rate_avg())"}],
    [{"sTitle":"Time (ms)"},{"content":"object.time_avg()"}],
    [{"sTitle":"Heap Memory (MB)"},{"content":"'%.3f'%(object.memory_used_avg()*1e-6)"}],
    ]

plot_view = {
    "plot":[
        {"name":"rate","data":("object.rate_avg()","math.log(object.tx_size(),2)"),"xaxis":"pow(2,Transaction size)"},
        {"name":"memory","data":("object.memory_used_avg()*1e-6","math.log(object.tx_size(),2)"),"xaxis":"pow(2,Transaction size)"},
        ],
    "ivar":[
        {"name":"Platform","id":"object.platform_id()","content":"object.platform()"},
        {"name":"Index Type","id":"object.index_type_id()","content":"object.index_type()"},
        ]
}


graph_size = pow(2,18)*10
query_size = pow(2,17)
cases = []

for tx_size in tx_sizes:
    no_index_case = {
        "name":"ingest",
        "description":"Vertex Ingestion as a function of transaction size (page_size=%d)."%(pow(2,14)),
        "type":"vertex_ingest",
        "data":
        {
            "template":["basic"],
            "config":["default:default"],
            "page_size":[14],
            "threads":[1],
            "use_index":[0],
            "new":1,
            "size":[graph_size],
            "txsize":[tx_size],
            "ig_version":["ig.3.1"]
            },
        
        "table_view":table_view,
        "plot_view":plot_view
        }
    cases.append(no_index_case)
    pass

for tx_size in tx_sizes:
    index_case = {
        "name":"ingest",
        "description":"Vertex Ingestion as a function of transaction size (page_size=%d)."%(pow(2,14)),
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
            "ig_version":["ig.3.1"]
            },
        "table_view":table_view,
        "plot_view":plot_view
        }
    query_case = {
        "name":"query",
        "description":"Vertex Query as a function of transaction size (graph_size=%d,query_size=%d)."%(graph_size,query_size),
        "type":"query",
        "data":
        {
            "template":["basic"],
            "vertex":["Node"],
            "config":["default:default"],
            "page_size":[14],
            "threads":[1],
            "txsize":[tx_size],
            "size":[query_size],
            "graph_size":[graph_size],
            "ig_version":["ig.3.0"]
            },
        "table_view":table_view,
        "plot_view":plot_view
        }   
    cases.append(index_case)
    cases.append(query_case)
    

    
    


    




    

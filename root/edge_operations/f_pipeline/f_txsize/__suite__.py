name = "Transaction Size (Pipeline Ingest)"
description = "Pipeline Edge Ingestion as a function of transaction size."

tx_sizes = []
for i in xrange(10,17):
    tx_sizes.append(pow(2,i))
    pass

table_view = [
    [{"sTitle":"Platform"},{"content":"object.platform()"}],
    [{"sTitle":"Version"},{"content":"object.engine()"}],
    [{"sTitle":"Transaction Size"},{"content":"object.tx_size()"}],
    [{"sTitle":"Rate (v/s)"},{"content":"'%.2f'%(object.rate_avg())"}],
    [{"sTitle":"Time (ms)"},{"content":"object.time_avg()"}]
    ]

plot_view = {
    "plot":[
        {"name":"rate","data":("object.rate_avg()","math.log(object.tx_size(),2)"),"xaxis":"pow(2,Transaction size)"},
        {"name":"time","data":("object.time_avg()*0.001","math.log(object.tx_size(),2)"),"xaxis":"pow(2,Transaction size)"},
        ],
    "ivar":[
        {"name":"Platform","id":"object.platform_id()","content":"object.platform()"},
        {"name":"Version","id":"object.engine_id()","content":"object.engine()"},
        ]
}

graph_size = pow(2,17)
cases = [
    {
    "name":"ingest",
    "description":"Edge Ingestion as a function of transaction size (page_size=%d)."%(pow(2,14)),
    "type":"pipeline_edge_ingest",
    "data":
    {
    "template":["basic"],
    "config":["default:default"],
    "page_size":[14],
    "threads":[1],
    "use_index":[1],
    "new":1,
    "txsize":tx_sizes,
    "size":[graph_size],
    "ig_version":["ig.3.1","ig.3.0"]
    },
    "table_view":table_view,
    "plot_view":plot_view
    }
    ]
    


    




    

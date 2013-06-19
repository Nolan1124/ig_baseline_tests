name = "Transaction Size"
description = "Vertex Ingestion as a function of transaction size."

txsize = []
for i in xrange(8,19):
    txsize.append(pow(2,i))
    pass

table_view = [
    [{"sTitle":"Database engine"},{"content":"object.engine()"}],
    [{"sTitle":"Graph Scale"},{"content":"'scale:%d'%(math.log(object.graph_size(),2))"}],
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


graph_size = pow(2,18)*80
cases = [
    {
        "name":"ingest",
        "description":"Vertex Ingestion as a function of transaction size (page_size=%d)."%(pow(2,14)),
        "type":"vertex_ingest",
        "data":
        {
            "template":["basic"],
            "config":["default:default"],
            "page_size":[14],
            "threads":[1],
            "use_index":[0,1],
            "new":1,
            "size":[graph_size],
            "txsize":txsize,
            "txlimit":[10],
            "ig_version":["ig.3.0"]
            },
        
        "table_view":table_view,
        "plot_view":plot_view
        }
    ]
    
    

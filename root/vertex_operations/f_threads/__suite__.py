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

graph_size = pow(2,14)*80
tx_size = pow(2,14)
page_size = 14
desc  =  "<p><b>Vertex Ingestion as a function of number of threads.</b></p>"
desc += "<p><strong>Graph Size = %d</strong></p>"%(graph_size)
desc += "<p><strong>Transaction Size = %d</strong></p>"%(tx_size)
desc += "<p><strong>Page Size = %d</strong></p>"%(pow(2,page_size))

cases = [
    {
        "name":"ingest",
        "description":"Vertex Ingestion as a function of number of threads. (transaction limit=%d, page size=%d, transaction size=%d)"%(10,pow(2,page_size),tx_size),
        "type":"vertex_ingest",
        "data":
        {
            "template":["basic"],
            "config":["default:default"],
            "page_size":[14],
            "threads":[1,2,3,4,5],
            "use_index":[0,1],
            "new":1,
            "size":[graph_size],
            "txsize":[tx_size],
            "txlimit":[10],
            "ig_version":["ig.3.0"]
            },
        "table_view":table_view,
        "plot_view":plot_view
        }
    ]

name = "Page size (Edge)"
description = "Edge Ingestion as a function of page size."

table_view = [
    [{"sTitle":"Platform"},{"content":"object.platform()"}],
    [{"sTitle":"Version"},{"content":"object.engine()"}],
    [{"sTitle":"Page size"},{"content":"object.page_size()"}],
    [{"sTitle":"Index Type"},{"content":"'index:%s'%(object.index_type())"}],
    [{"sTitle":"Rate (e/s)"},{"content":"'%.2f'%(object.rate_avg())"}]
    ]

plot_view = {
    "plot":[
        {"name":"rate","data":("object.rate_avg()","object.page_size()"),"xaxis":"page size = pow(2,x)"},
        {"name":"memory","data":("object.memory_used_avg()*1e-6","math.log(object.page_size(),2)"),"xaxis":"page size = pow(2,x)"},
        ],
    "ivar":[
        {"name":"Platform","id":"object.platform_id()","content":"object.platform()"},
        {"name":"Index Type","id":"object.index_type_id()","content":"object.index_type()"},
        {"name":"Version","id":"object.engine_id()","content":"object.engine()"},
        ]
    }

txsize = pow(2,14)
graph_size = pow(2,20)
page_sizes = [16,15,14,13,12,11,10]
cases = [
    {
        "name":"ingest",
        "description":"Edge Ingestion as a function of page size (transaction_size=%d graph_size=%d)."%(txsize,graph_size),
        "type":"edge_ingest",
        "data":
        {
            "template":["basic"],
            "config":["default:default"],
            "page_size":page_sizes,
            "threads":[1],
            "use_index":[1],
            "new":1,
            "txsize":[txsize],
            "size":[graph_size],
            "ig_version":["ig.3.0","ig.3.1"]
            },
        "table_view":table_view,
        "plot_view":plot_view
        }
    ]

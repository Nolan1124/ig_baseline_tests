name = "Disks"
description = "Vertex Ingestion as a function of number of threads/processes and disks."

table_view = [
    [{"sTitle":"Database engine"},{"content":"object.engine()"}],
    [{"sTitle":"Graph Size"},{"content":"object.graph_size()"}],
    [{"sTitle":"Threads"},{"content":"object.threads()"}],
    [{"sTitle":"Processes"},{"content":"object.processes()"}],
    [{"sTitle":"Config"},{"content":"'{0}'.format(object.config())"}],
    [{"sTitle":"Index Type"},{"content":"'index:%s'%(object.index_type())"}],
    [{"sTitle":"Rate (v/s)"},{"content":"'%.2f'%(object.rate_avg())"}],
    [{"sTitle":"Time (ms)"},{"content":"object.time_avg()"}],
    ]

plot_view = {
    "plot":[
        {"name":"rate","data":("object.rate_avg()","object.threads()"),"xaxis":"Threads"},
        {"name":"time","data":("object.time_avg()","object.threads()"),"xaxis":"Threads"},
        ],
    "ivar":[
        {"name":"Platform","id":"object.platform_id()","content":"object.platform()"},
        {"name":"Index Type","id":"object.index_type_id()","content":"object.index_type()"},
        {"name":"Index Type","id":"object.config_id()","content":"object.config()"},
        {"name":"Version","id":"object.engine_id()","content":"object.engine()"},
        {"name":"Processes","id":"object.processes()","content":"object.processes()"},
        ]
    }

graph_size = pow(2,22)
tx_size = pow(2,14)
page_size = 14

cases = [
    {
        "name":"ingest",
        "description":"Vertex Ingestion as a function of number of threads/processes and disks. (transaction limit=%d, page size=%d, transaction size=%d)"%(10,pow(2,page_size),tx_size),
        "type":"vertex_ingest",
        "data":
        {
            "template":["basic_non_unique"],
            "config":["local_disks:1","local_disks:2","local_disks:3","local_disks:4"],
            "page_size":[14],
            "threads":[1,2,4],
            "processes":[(None,1),(None,2),(None,3),(None,4)],
            "use_index":[0,1],
            "new":1,
            "size":[graph_size],
            "txsize":[tx_size],
            "ig_version":["ig.3.2","ig.3.1"]
            },
        "table_view":table_view,
        "plot_view":plot_view
        }
    ]

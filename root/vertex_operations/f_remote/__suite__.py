name = "Remote"
description = "Vertex Ingestion/Query using remote storage and/or remote lock server."

table_view = [
    [{"sTitle":"Version"},{"content":"object.engine()"}],
    [{"sTitle":"Graph Size"},{"content":"object.graph_size()"}],
    [{"sTitle":"Threads"},{"content":"'T:%d'%(object.threads())"}],
    [{"sTitle":"Config"},{"content":"'{0}'.format(object.config())"}],
    [{"sTitle":"Index Type"},{"content":"'index:%s'%(object.index_type())"}],
    [{"sTitle":"Rate (v/s)"},{"content":"'%.2f'%(object.rate_avg())"}],
    [{"sTitle":"Time (ms)"},{"content":"object.time_avg()"}]
    ]

plot_view = {
    "plot":[
        {"name":"rate","data":("object.rate_avg()","object.threads()"),"xaxis":"Threads"},
        {"name":"time","data":("object.time_avg()","object.threads()"),"xaxis":"Threads"},
        ],
    "ivar":[
        {"name":"Platform","id":"object.platform_id()","content":"object.platform()"},
        {"name":"Index Type","id":"object.index_type_id()","content":"object.index_type()"},
        {"name":"Config","id":"object.config_id()","content":"object.config()"},
        {"name":"Version","id":"object.engine_id()","content":"object.engine()"},
        {"name":"Page Size","id":"object.page_size()","content":"object.page_size()"},
        ]
    }

graph_size = pow(2,21)
tx_size = pow(2,14)
page_size = [12,14,16]

cases = [
    {
        "name":"ingest",
        "description":"Vertex Ingestion as a function of number of threads and configs. (transaction limit={0}, page size={1}, transaction size={2})".format(10,str(page_size),tx_size),
        "type":"vertex_ingest",
        "data":
        {
            "template":["basic"],
            "config":["remote_host:local_lockserver.disk.1",
                      "remote_host:remote_lockserver.disk.1",
                      "local_host:local_lockserver.disk.1",
                      "local_host:remote_lockserver.disk.1",
                      ],
            "page_size":page_size,
            "threads":[1,2,4,8,16],
            "use_index":[0],
            "new":1,
            "size":[graph_size],
            "txsize":[tx_size],
            "txlimit":[-1],
            "ig_version":["ig.3.1","ig.3.2"]
            },
        "table_view":table_view,
        "plot_view":plot_view
        }
    ]

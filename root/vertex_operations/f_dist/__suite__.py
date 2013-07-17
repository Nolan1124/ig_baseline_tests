name = "Distributed"
description = "Distributed Vertex Ingest/Query"

table_view = [
    [{"sTitle":"Version"},{"content":"object.engine()"}],
    [{"sTitle":"Platform"},{"content":"object.platform()"}],
    [{"sTitle":"Process"},{"content":"'%d'%(object.processes())"}],
    [{"sTitle":"Setup"},{"content":"object.process_description()"}],
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
        {"name":"Process Setup","id":"object.process_description_id()","content":"object.process_description()"},
        ]
    }

graph_size = pow(2,20)
query_size = pow(2,15)
tx_size = pow(2,14)
page_size = 14
cases = []
processes = []
num_proc = 16

def generate_case(_processes_,_graph_size_,_new_,name="ingest"):
    return {
        "name":name,
        "description":"Vertex Ingestion as a function of hosts (page size=%d, transaction size=%d)"%(pow(2,page_size),tx_size),
        "type":"vertex_ingest",
        "data":
        {
            "template":["basic_non_unique"],
            "config":["dist_host:host1"],
            "page_size":[14],
            "threads":[1],
            "use_index":[0],
            "new":_new_,
            "txsize":[tx_size],
            "size":[_graph_size_],
            "ig_version":["ig.3.1"],
            "process":_processes_,
            },
        "table_view":table_view,
        "plot_view":plot_view
        }

init_case = generate_case([([0],1)],1,1,"initial_ingest") 

#machine 0 only setup
for i in xrange(num_proc):
    process = [(([0],i+1))]
    cases.append(init_case)
    cases.append(generate_case(process,graph_size,0))
    pass

#machine 1 only setup
for i in xrange(num_proc):
    process = [([1],i+1)]
    cases.append(init_case)
    cases.append(generate_case(process,graph_size,0))
    pass


#local+remote machine setup
for i in xrange(num_proc):
    process = [([0,1],i+1)]
    cases.append(init_case)
    cases.append(generate_case(process,graph_size,0))
    pass

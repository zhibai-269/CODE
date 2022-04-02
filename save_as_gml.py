with open("graph.gml", "w") as f:
    for i in nodes:
        f.write("\t\t<node id=\"" + str(i) + "\" label=\"" + str(i) + "\"/>\n")
    for i in edges:
        f.write("\t\t<edge source=\"" + str(i[0]) + "\" target=\"" + str(i[1]) + "\"/>\n")
    f.write("\t</graph>\n</gexf>")

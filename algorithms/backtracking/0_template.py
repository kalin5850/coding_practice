def dfs(start_idx, path):
    if is_leaf(start_idx):
        report(path)
        return
    for edge in get_edges(start_idx):
        path.add(edge)
        dfs(start_idx + 1, path)
        path.pop()

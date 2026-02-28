class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def BuildTree(records):
    if not records:
        return None

    records.sort(key=lambda x: x.record_id)

    if records[-1].record_id != len(records) - 1:
        raise ValueError('Record id is invalid or out of order.')

    if any(record.record_id < record.parent_id for record in records):
        raise ValueError('Node parent_id should be smaller than its record_id.')

    if any(record.record_id == record.parent_id for record in records if record.record_id != 0):
        raise ValueError('Only root should have equal record and parent id.')

    nodes = {0: Node(0)}

    for record in records[1:]:
        new_node = Node(record.record_id)
        nodes[record.record_id] = new_node
        nodes[record.parent_id].children.append(new_node)

    return nodes[0]

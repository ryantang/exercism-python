from itertools import islice

class Record:
    """Represents a raw record with an ID and a parent ID."""

    def __init__(self, record_id: int, parent_id: int) -> None:
        """Initialize a record with its ID and parent ID."""
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    """Represents a node in a tree, with an ID and a list of child nodes."""

    def __init__(self, node_id: int) -> None:
        """Initialize a node with its ID and an empty children list."""
        self.node_id = node_id
        self.children: list["Node"] = []


def build_tree(records: list[Record]) -> Node | None:
    """
    Build a tree from a list of Record objects.

    Records are sorted and validated before building the tree.
    Returns the root Node, or None if the records list is empty.

    Raises ValueError if record IDs are invalid, out of order,
    or if parent/child relationships are inconsistent.
    """
    if not records:
        return None

    records.sort(key=lambda x: x.record_id)

    # Ensure record IDs start from zero and count up in order
    for index, record in enumerate(records):
        if record.record_id != index:
            raise ValueError('Record id is invalid or out of order.')

    if any(record.record_id < record.parent_id for record in records):
        raise ValueError('Node parent_id should be smaller than its record_id.')

    if any(record.record_id == record.parent_id for record in records if record.record_id != 0):
        raise ValueError('Only root should have equal record and parent id.')

    nodes = {0: Node(0)}

    for record in islice(records, 1, None):
        new_node = Node(record.record_id)
        nodes[record.record_id] = new_node
        nodes[record.parent_id].children.append(new_node)

    return nodes[0]

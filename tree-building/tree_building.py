from dataclasses import dataclass, field
from itertools import islice

@dataclass
class Record:
    """Represents a raw record with an ID and a parent ID."""
    record_id: int
    parent_id: int


@dataclass
class Node:
    """Represents a node in a tree, with an ID and a list of child nodes."""
    node_id: int
    children: list["Node"] = field(default_factory=list)


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

    nodes = {0: Node(node_id=0)} #seed with root node

    for record in islice(records, 1, None): #skip pre-seeded root node
        new_node = Node(node_id=record.record_id)
        nodes[record.record_id] = new_node
        nodes[record.parent_id].children.append(new_node)

    return nodes[0]

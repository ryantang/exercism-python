from itertools import takewhile

CODON_MAP = {
    'AUG': 'Methionine',
    'UUU': 'Phenylalanine',
    'UUC': 'Phenylalanine',
    'UUA': 'Leucine',
    'UUG': 'Leucine',
    'UCU': 'Serine',
    'UCC': 'Serine',
    'UCA': 'Serine',
    'UCG': 'Serine',
    'UAU': 'Tyrosine',
    'UAC': 'Tyrosine',
    'UGU': 'Cysteine',
    'UGC': 'Cysteine',
    'UGG': 'Tryptophan',
    'UAA': 'STOP',
    'UAG': 'STOP',
    'UGA': 'STOP'
}


def proteins(strand):

    triplets = (
        strand[i:i+3] 
        for i in range(0, len(strand), 3)
    )

    codons = (CODON_MAP[triplet] for triplet in triplets)

    codons_upto_stop = list(
        takewhile(lambda codon: codon != 'STOP', codons)
    )
    
    return codons_upto_stop

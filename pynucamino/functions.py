from .nucalign import Nucamino


def align(*, seqs, profile, genes, check=True):
    '''Align a fasta-formatted collection of nucleotide sequences using
    the given profile name and iterable of gene names

    See :class:`Nucamino` for details about the arguments.
    '''
    alignment = Nucamino(
        seqs=seqs,
        profile=profile,
        genes=genes,
        check=check,
    )
    return alignment.result

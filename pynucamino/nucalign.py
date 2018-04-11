import json
import subprocess


class NucAlignment(object):

    @classmethod
    def _nucalign(cls, inputseqs, profile, genes, check=True):
        gene = ",".join(g.upper() for g in genes)
        command = ["./nucamino", "align", profile, gene, "-q", "-f", "json"]
        if type(inputseqs) is not bytes:
            inputseqs = bytes(inputseqs, 'utf8')
        align_proc = subprocess.run(
            command,
            input=inputseqs,
            stdout=subprocess.PIPE,
        )
        if check:
            align_proc.check_returncode()
        outp = align_proc.stdout.decode('utf8')
        return json.loads(outp), align_proc

    def __init__(self, seq, profile, genes):
        '''Perform and alignment and store the results.

        Arguments:

          - :param seq:`seq`: The sequence to align (as a FASTA formatted
            string).
          - :param profile:`profile`: The name of the alignment profile to use
            while aligning (e.g. `hcv1a`, `hiv1b`).
          - :param genes:`genes`: An iterable of genes to try aligning against.
        '''
        self.result, self.proc = self._nucalign(
            seq,
            gene=genes,
            profile=profile,
        )

# saturation_mutagenesis_be
 When given a text file of base pairs, this will return it as all possible guide RNAs for editing the 4th, 5th, or 6th position with ABEs and CBEs.
 These positions were determined empirically to be the highest efficiency edits.

 Exons 2,3,4 from APOE were used to generate saturation mutagenesis gRNAs.
 When selecting sequences from exons, 20bp excess was included on both sides as a buffer. This ensures that both forward and reverse guides can be correctly assigned for possible edits on the edges of the exons.

 All of exon 2 was used, including non-signal sequence/non-CDS. All of exon 3 was used. Only the coding sequence of exon 4 was used, and the STOP codon was included in the non-buffer area (can be possibly mutated)

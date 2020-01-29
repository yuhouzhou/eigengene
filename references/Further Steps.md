1. Apply the workflow to different models. One of them should be RECON. ***I found "Recon3D" and "RECON1" in BiGG database, which one should I use？***
2. Try to look at other eigen-values. 1st and 2nd smallest, middle, and largest, in order to see the change of smoothness.
3. For RECON: Run the workflow on the gene about all compartments; Run the workflow on the gene only about cytosol.
4. Gene Expression Omnibus （GEO） database: Compare with gene expression activity vectors. 
   * Decide which gene expression vectors are to be used. 
   * Compute Correlation Coefficients （both Pearson's and Spearman's）between the selected vectors and eigenvectors. Pick up the maximum.
   * Shuffle the gene expression entries, and repeat the previous step. The shuffle one should have worse significance.
   * Do the previous step several times to get a p-value distribution.
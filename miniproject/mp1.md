# Mini Project 1 Competency Claim

This project demonstrates **C3 (Data cleaning and file handling)** because I programmatically collected data from PokéAPI, transformed nested JSON into a structured pandas DataFrame, and engineered analysis-ready fields such as `total_stats` and grouped indicators for comparison. I also handled expected missingness (for example, `secondary_type` for single-type Pokemon) and documented why those nulls are structurally valid rather than data errors.

This work demonstrates **C5 (Data analysis with pandas)** through question-driven analysis using correlations, grouped summaries, effect-size calculations, and a permutation-based significance test. I used these methods to evaluate relationships among size and speed, quantify type-level specialization patterns, and compare low-ID and high-ID Pokemon on total base stats.

This project demonstrates **C6 (Data visualization)** by building a Plotly scatter chart that aligns with the analysis claim, uses appropriate encodings for multiple variables, and includes clear titles and labels for interpretability. I selected chart structure intentionally so readers can compare trend direction and variation across Pokemon types.

This project demonstrates **C7 (Critical evaluation and professional judgment)** because I interpreted results with appropriate caution, stated assumptions (such as using Pokédex ID as a proxy for iconicity), and identified limits on generalization (single generation, base stats only, non-causal interpretation). These decisions show evidence of analytic reasoning beyond producing code outputs.

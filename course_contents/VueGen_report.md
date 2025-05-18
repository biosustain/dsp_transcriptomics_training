# Analysis reporting with Vuegen

In the GitHub workspace, we will use the base conda environment which you can activate
with the following command:

```bash
conda activate base
```

## Install the required packages

- [vuegen](https://vuegen.readthedocs.io) for the report generation (developed by Henry Webel from DSP and Sebastian Ayala and Alberto Santos from MoNA at DTU Biosustain)

```bash
pip install vuegen
```

## VueGen Report

We saved some of the analyses (plots and tables) from the R markdown to `results/report` folder. 

You can use the following command to generate a VueGen report from them:

```bash
vuegen -dir results/report
```

This will create a streamlit app in the `streamlit_report` folder. Check the options 
availble for the command line tool vuegen with the following command:

```
vuegen -h
```

Create and start the streamlit app with the following command:

```bash
vuegen -dir results/report -st_autorun
```

### VueGen GUI (app)

If you are interested to know more about VueGen and used for your own research projects check out some tutorials in youtube
[tutorials on youtube](https://www.youtube.com/playlist?list=PLTbkQyef1c2S3qGzzva_JLlgdwsXjHCHH), and also our [paper](https://www.biorxiv.org/content/10.1101/2025.03.05.641152v1.full.pdf)

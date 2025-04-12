# Instructions

## Opening the Nextflow environment

To avoid installation and configuration issues we are going to deploy an environment for you containing Nextflow and its requirements.

If you want to open directly a GitHub codespace for this specific repository click here: [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/biosustain/dsp_transcriptomics_training)

Don't change the configuration and accept the default option. It says pay but you're not paying...

If you want to do it manually go to [course website](https://github.com/biosustain/dsp_transcriptomics_training)

Click on button **Code** and click on the Codespaces tab. There click on **Create codespace**. Now your Nextflow environment will be built following the instructions in devcontainer.json file (i.e. installing Ubuntu, Docker, Nextflow, R, Python, VSCode and RStudio server)

To learn more about Github codespaces go [here](https://github.com/features/codespaces)

>Please remember to delete your Codespace by the end of the class so that you do not consume your free Github codespace credits! If you do not delete it it will be deleted automatically days after you created.

## Initial checks
Now, Nextflow should be ready to run in your GitHub Codespace environment! Let's check that you have a fully functional environment with Nextflow, java and Docker properly installed

```{code-block} bash
:caption: Verify java installation:

java -version
```

```{code-block} bash
:caption: Verify Nextflow installation:

nextflow -v
```

```{code-block} bash
:caption: Nextflow current version, system and runtime:

nextflow info
```

```{code-block} bash
:caption: Verify Docker installation:

docker --version
```

If everything went well you have a fully functional Nextflow environment for today. Rememeber that we are going to use VS code as our editor to write code and handle our files.

To check if you have access to RStudio go to the Ports tab and click on "Open in Browser", this will deploy the RStudio for the downstream analysis.
# Neural Networks For GWAS

_A final project for DS 4440 - Neural Networks_ 

Using the python library [Selene](https://github.com/FunctionLab/selene) to enable applications of neural networks to Genome Wide Association Studies. 

## Instructions for running training: 
You will need to upload this directory to Google Drive, where you can train the models by opening `run_training.ipynb` in Colab and running each of the cells.
- Data can be downloaded and processed by following the instructions in `getting_started_with_selene.ipynb`.
- To select which model is used, simply update the two relevant lines in `training_configs.yml`.
- Information about the training (loss and precision) will be logged periodically in colab. To get the raw data from the logs, copy them into their own `.log` file and use `scripts/scrape_log_values.py` to extract the raw list of values. These values can then be used to visualize the results. 

## Important files
- `run_training.ipynb` loads data files and runs training in colab
- `training_configs.yml` contains all of the configurations for training, which can be updated to train a different model, change the length of training, or change the way that logs are generated. 
- `getting_started_with_selene.ipynb` contains instructions for preparing data and installing Selene. This file was copied from a tutorial in the [Selene GitHub repo](https://github.com/FunctionLab/selene/tree/master/tutorials). 
- `visualize_results.ipynb` contains visualizations to compare the performance of each model. 


_View the colab files and data in [Google Drive](https://drive.google.com/drive/folders/1FBa4NZN894Q67BuwB6AkCpb3plWRZ_XB?usp=sharing)._ 